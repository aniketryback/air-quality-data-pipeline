import pandas as pd
import os
import requests
from datetime import datetime
API_TOKEN = "9e0d6f1b6abe8d9de61c9051a41a3fc1d4e7db41"
def fetch_city_aqi(city = "Delhi"):
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        print(f"❌ Failed to fetch data for {city}")
        return pd.DataFrame()

    aqi_data = data["data"]
    return {
        "city": city,
        "aqi": aqi_data["aqi"],
        "pm25": aqi_data["iaqi"].get("pm25", {}).get("v", None),
        "pm10": aqi_data["iaqi"].get("pm10", {}).get("v", None),
        "temperature": aqi_data["iaqi"].get("t", {}).get("v", None),
        "humidity": aqi_data["iaqi"].get("h", {}).get("v", None),
        "timestamp": aqi_data["time"]["s"]
    }
    
def fetch_multiple_cities(city_list):
    results = []
    for city in city_list:
        record = fetch_city_aqi(city)
        if isinstance(record, dict):   # ✅ confirm it's a valid dictionary
            results.append(record)
    return pd.DataFrame(results)

if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)

    cities = ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai"]
    df = fetch_multiple_cities(cities)

    if not df.empty:
        filename = f"data/processed/aqi_multiple_cities_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved AQI data for multiple cities to {filename}")
    else:
        print("⚠️ No data collected.")