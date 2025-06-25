import pandas as pd
import os


def get_latest_file(folder, prefix ="aqi_multiple_cities_", ext = ".csv"):
    files = [f for f in os.listdir(folder) if f.startswith(prefix) and f.endswith(ext)]

    files.sort(reverse = True)
    return os.path.join(folder, files[0])

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df[["city", "aqi", "pm25", "pm10", "temperature", "humidity", "timestamp"]]

    df = df.dropna(subset=["pm25","aqi"])

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df = df.sort_values("timestamp")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index = False)

    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    input_file = "data/processed/aqi_multiple_cities_20250625_1522.csv"
    output_file = "data/processed/aqi_multiple_cities_cleaned.csv"
    clean_data(input_file, output_file)