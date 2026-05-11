import requests
import pandas as pd
import os

print("Starting data collection...")

# Create dataset folder automatically
os.makedirs("dataset", exist_ok=True)

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

try:
    response = requests.get(url)

    print("API Status Code:", response.status_code)

    data = response.json()

    earthquakes = []

    for feature in data['features']:

        properties = feature['properties']
        geometry = feature['geometry']

        earthquakes.append({
            'magnitude': properties['mag'],
            'place': properties['place'],
            'time': properties['time'],
            'longitude': geometry['coordinates'][0],
            'latitude': geometry['coordinates'][1],
            'depth': geometry['coordinates'][2]
        })

    df = pd.DataFrame(earthquakes)

    print(df.head())

    # Save file
    file_path = "dataset/earthquake_data.csv"

    df.to_csv(file_path, index=False)

    print(f"CSV file saved at: {file_path}")

except Exception as e:
    print("ERROR:", e)