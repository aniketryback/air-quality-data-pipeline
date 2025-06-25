# 🌫️ Air Quality Data Pipeline (India Cities)

This project is a complete end-to-end **Data Engineering pipeline** that fetches live AQI (Air Quality Index) data for multiple Indian cities using the **WAQI API**, transforms and cleans the data, and visualizes PM2.5 levels across cities.

---

## 🚀 Features

- 🔁 **Live data ingestion** using WAQI public API
- 🧼 **Transformation**: Cleans, filters, and standardizes AQI, PM2.5, PM10, temperature, and humidity
- 📊 **Visualization**: Plots PM2.5 levels across cities using Matplotlib and Seaborn
- 📁 **Organized pipeline structure** with auto-file detection and timestamping
- 💾 **Scalable**: Easily extendable to include S3 upload, scheduling (Airflow), or time-series tracking

---

## ⚙️ Tech Stack

| Tool       | Use                         |
|------------|------------------------------|
| Python     | Core scripting and ETL       |
| Pandas     | Data processing              |
| Requests   | API integration              |
| Matplotlib / Seaborn | Visualizations     |
| WAQI API   | Live air quality data        |

---

## 📂 Project Structure

air-quality-pipeline/
├── ingest.py # Pulls real-time AQI from WAQI API
├── transform.py # Cleans and standardizes the data
├── plot.py # Visualizes PM2.5 by city
├── config.ini (optional) # API keys (add to .gitignore)
├── data/
│ └── processed/
│ ├── aqi_multiple_cities_<timestamp>.csv
│ └── aqi_multiple_cities_cleaned.csv
├── output/
│ └── pm25_by_city.png
└── README.md
