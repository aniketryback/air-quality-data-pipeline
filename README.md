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

## ☁️ Cloud Integration (AWS S3)

This pipeline is now cloud-enabled!

- ✅ Automatically uploads the cleaned CSV to an AWS S3 bucket
- ✅ Uses `boto3` to push the latest `aqi_multiple_cities_*.csv` to the cloud
- ✅ Prepares the dataset for future integration with PySpark, Glue, Athena, or Redshift

```python
# sample output
✅ Uploaded data/processed/aqi_multiple_cities_20250621_1532.csv to s3://aqi-data-aniket/aqi_multiple_cities_20250621_1532.csv
```
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
