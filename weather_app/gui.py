# gui.py
import tkinter as tk
from tkinter import messagebox
from logic import fetch_weather_data
from utils import load_preferences, save_preferences

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather App")
        self.root.geometry("300x200")
        
        self.city_var = tk.StringVar()
        self.weather_info = tk.StringVar()

        self.create_widgets()

        # Load last searched city from preferences
        last_city = load_preferences()
        if last_city:
            self.city_var.set(last_city)
            self.get_weather()

    def create_widgets(self):
        tk.Label(self.root, text="Enter City:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.city_var).pack(pady=5)
        
        tk.Button(self.root, text="Get Weather", command=self.get_weather).pack(pady=10)
        tk.Label(self.root, textvariable=self.weather_info).pack(pady=10)

    def get_weather(self):
        city = self.city_var.get()
        if city:
            try:
                data = fetch_weather_data(city)
                self.weather_info.set(f"Temperature: {data['temp']}°C\n{data['description']}")
                save_preferences(city)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a city name")

    def run(self):
        self.root.mainloop()
