 🌍 AI Earthquake Prediction System

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
 Step :  Run application
streamlit run app.py

📊 OUTPUT (Project Results)

🏠 1. Dashboard Output
The dashboard displays real-time earthquake statistics:
<img width="1827" height="876" alt="image" src="https://github.com/user-attachments/assets/484d53ed-602a-4ab0-b92b-5d10cb0fb26f" />
<img width="1853" height="781" alt="image" src="https://github.com/user-attachments/assets/bde27a28-0eaf-46cd-a651-b82fc2b4127b" />

📈 2. Data Visualization Output
The system generates analytical graphs:
<img width="1847" height="845" alt="image" src="https://github.com/user-attachments/assets/01703a7c-f3b7-4665-87fc-8d979dc414aa" />
<img width="1393" height="556" alt="image" src="https://github.com/user-attachments/assets/9baba4ef-ffeb-4dec-addd-cb5c94e2ef3c" />

🗺️ 3. Live Map Output
Interactive world map showing earthquake locations:
<img width="1832" height="840" alt="image" src="https://github.com/user-attachments/assets/bf54d300-f581-4a52-881d-988dfa257821" />

🟢 Green Marker → Low Risk
🟡 Yellow Marker → Medium Risk
🔴 Red Marker → High Risk
Each marker displays:
Location
Magnitude
Depth
Timestamp

🔥 4. Heatmap Output
<img width="1793" height="823" alt="image" src="https://github.com/user-attachments/assets/69de5304-da71-495a-bf56-6aa3d7d98f74" />
Shows high-density seismic zones
Identifies earthquake-prone regions globally
Highlights clusters of seismic activity

🤖 5. AI Prediction Output
Machine Learning model predicts earthquake risk based on:
<img width="1480" height="707" alt="image" src="https://github.com/user-attachments/assets/97f2d8ee-06a3-4589-a9c1-8d0cadc3401c" />
Latitude
Longitude
Depth
Example Output:

Predicted Magnitude: 4.18 
Risk Level: Moderate 

🚨 6. Alert System Output

When a high-risk earthquake is detected:

📧 Email Alert Sent:
Subject: ⚠ Earthquake Alert Notification

Message:
High magnitude earthquake detected!

Location: [Latitude, Longitude]
Magnitude: 6.8
Risk Level: HIGH

Please take necessary precautions.

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
