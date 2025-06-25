import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_data(input_path):

    df = pd.read_csv(input_path)

    plt.figure(figsize=(10,8))
    sns.barplot(x="city", y="pm25", data=df, palette="mako")

    plt.xlabel("city")
    plt.ylabel("PM 2.5")
    plt.title("PM2.5 Levels by City")
    plt.tight_layout()
    
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/pm25_by_city.png")
    print("✅ PM2.5 plot saved to output/pm25_by_city.png")

if __name__ == "__main__":
    plot_data("data/processed/aqi_multiple_cities_cleaned.csv")

