# Earthquake-Prediction-App
# 🌍 AI Earthquake Prediction System

An advanced AI + Machine Learning based Earthquake Prediction and Monitoring System that uses real-time seismic data from USGS and provides intelligent analytics, visualization, and anomaly detection.

## 👩‍💻 Author
**Janhavi Phale**

## 🚀 Project Overview

This project is designed to:
- Predict earthquake risk using Machine Learning
- Analyze real-time seismic activity
- Detect anomalies in earthquake patterns
- Visualize earthquake data using maps and graphs
- Provide dashboard analytics for decision making

## ⚙️ Features

- 🌐 Real-time Earthquake Data (USGS API)
- 🤖 Machine Learning Prediction Model
- 📊 Dashboard Analytics
- 🗺️ Interactive Live Map (Folium)
- 🔥 Heatmap Visualization
- 📈 Graphs (Magnitude, Depth, Trends)
- 🚨 AI Anomaly Detection (Isolation Forest)
- 📧 Email Alert System
- 🎯 Risk Level Classification

## 🧠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Folium
- Requests
- USGS Earthquake API

## 📂 Project Structure
EarthquakePrediction/
│
├── app.py
├── train_model.py
├── data_collection.py
├── email_alert.py
├── earthquake_model.pkl
├── dataset/
│ └── earthquake_data.csv
├── requirements.txt

## ▶️ How to Run Project

### Step 1: Install dependencies

pip install -r requirements.txt
Step 2: Run application
streamlit run app.py

📊 Output Screenshots
🔹 Dashboard View
Total Earthquakes
Average Magnitude
Maximum Magnitude
Live alerts for high-risk earthquakes
🔹 Visualization Output
Depth vs Magnitude Graph
Magnitude Distribution Histogram
Risk Pie Chart
Trend Line Graph
🔹 Live Map Output
Earthquake locations marked on world map
Color-coded markers:
🟢 Low Risk
🟡 Medium Risk
🔴 High Risk
🔹 Heatmap Output
Dense seismic activity zones highlighted
🔹 AI Prediction Output
Predicted magnitude based on:
Latitude
Longitude
Depth

Example:

Predicted Magnitude: 5.3
Risk Level: Moderate / Dangerous
🚨 Alert System

When magnitude is high:

Email alert is triggered automatically
Dashboard shows warning banner
Live notification appears in UI

Example Alert:

⚠️ ALERT: High Magnitude Earthquake Detected!
