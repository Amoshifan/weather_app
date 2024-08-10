# utils.py
import json
import os

PREFERENCES_FILE = "data/preferences.json"
def save_preferences(city):
    with open(PREFERENCES_FILE, 'w') as f:
        json.dump({'last_city': city}, f)

def load_preferences():
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, 'r') as f:
            data = json.load(f)
            return data.get('last_city')
    return None
