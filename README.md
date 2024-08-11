README.md
Simple Desktop Weather Application
Overview
This is a Python-based desktop weather application that provides real-time weather information for any specified city.
The application uses the OpenWeatherMap API to fetch current weather data and displays it in a simple graphical user 
interface (GUI) built with Tkinter.

Features
Fetch Weather Data: Retrieves current weather data from the OpenWeatherMap API.
Display Weather Information: Shows the temperature, weather conditions, and other relevant details.
User Input: Allows users to input a city name to retrieve weather information.
Error Handling: Manages errors such as invalid city names or network issues with appropriate messages.
Save Preferences: Stores the last searched city and automatically loads it on startup for convenience.
Technologies Used
Python: Core programming language used for the application logic.
Tkinter: GUI framework used to create the application's graphical interface.
OpenWeatherMap API: External API service used to fetch weather data.
JSON: Used for saving and loading user preferences.

Getting Started
Prerequisites
Python 3.x installed on your system.
An API key from OpenWeatherMap (free tier available).
Installation
Clone the repository:

git clone https://github.com/yourusername/weather-app.git
Navigate to the project directory:

cd weather-app
Install the required dependencies:

pip install -r requirements.txt
How to Use
Obtain your OpenWeatherMap API key and add it to the config.py file:

API_KEY = "1297c548bd5fb6de8d35ee4f192ffce1"
Run the application:

python main.py
Enter the city name in the provided input field and click "Get Weather" to view the weather information.
Example
Here is a simple example of how the application works:

Enter "Makurdi" in the input field.
Click "Get Weather."
The application will display the current temperature, weather conditions, and more for Makurdi.
Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. 
Pull requests are warmly welcome.

Author
Kwaghfan, Aondover Amos - https://github.com/Amoshifan

License
This project is licensed under the MIT License. - see the LICENSE file for details.
MIT License

Copyright (c) 2024 Kwaghfan, Aondover Amos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This README gives a comprehensive overview of your project, including how to get started, 
use the application, and contribute to it. Make sure to adjust any placeholder information 
like URLs or names as necessary.
