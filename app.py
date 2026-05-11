import streamlit as st
import pandas as pd
import requests
import joblib
import folium
import matplotlib.pyplot as plt

from streamlit_folium import folium_static
from folium.plugins import HeatMap
from streamlit_autorefresh import st_autorefresh
from sklearn.ensemble import IsolationForest
from streamlit_extras.metric_cards import style_metric_cards

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Earthquake Prediction System",
    page_icon="🌍",
    layout="wide"
)

# =====================================================
# AUTO REFRESH
# =====================================================

st_autorefresh(
    interval=60000,
    key="earthquake_refresh"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: white;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #00E5FF;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.stMetric label {
    color: white !important;
    font-size: 18px !important;
}

.stMetric div {
    color: #00E5FF !important;
    font-size: 30px !important;
    font-weight: bold !important;
}

div.stButton > button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("earthquake_model.pkl")

# =====================================================
# LOAD LIVE DATA
# =====================================================

@st.cache_data
def load_data():

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    response = requests.get(url)

    data = response.json()

    earthquakes = []

    for feature in data['features']:

        properties = feature['properties']
        geometry = feature['geometry']

        earthquakes.append({
            'magnitude': properties['mag'],
            'place': properties['place'],
            'longitude': geometry['coordinates'][0],
            'latitude': geometry['coordinates'][1],
            'depth': geometry['coordinates'][2]
        })

    df = pd.DataFrame(earthquakes)

    df.dropna(inplace=True)

    return df

# =====================================================
# LOADING ANIMATION
# =====================================================

with st.spinner("Loading Real-Time Earthquake Data..."):

    df = load_data()

# =====================================================
# AI ANOMALY DETECTION
# =====================================================

features = df[['magnitude', 'depth']]

anomaly_model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df['anomaly'] = anomaly_model.fit_predict(features)

# =====================================================
# EMAIL ALERT FUNCTION
# =====================================================

def send_email_alert(message):

    st.toast(
        f"📧 Email Alert Sent: {message}",
        icon="🚨"
    )

# =====================================================
# LIVE ALERTS
# =====================================================

high_risk = df[df['magnitude'] >= 5]

if len(high_risk) > 0:

    st.error(
        f"⚠️ ALERT: {len(high_risk)} High Magnitude Earthquakes Detected!"
    )

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2920/2920244.png",
    width=120
)

st.sidebar.title("🌍 Navigation")

menu = st.sidebar.radio(
    "Select Menu",
    [
        "Home",
        "Live Data",
        "Prediction",
        "Visualization",
        "Live Map",
        "Heatmap",
        "AI Anomaly Detection",
        "Dashboard Analytics"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if menu == "Home":

    st.markdown("""
    <h1 style='text-align:center;color:white;'>
    🌍 AI Earthquake Prediction & Monitoring System
    </h1>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1527489377706-5bf97e608852",
        use_container_width=True
    )

    st.markdown("""
    ## AI + Machine Learning Based Seismic Analysis

    This system uses:
    - Real-time earthquake data
    - Machine learning prediction
    - AI anomaly detection
    - Heatmaps
    - Dashboard analytics
    - Live notifications
    - Email alerts
    """)

    total_eq = len(df)

    avg_mag = round(df['magnitude'].mean(), 2)

    max_mag = round(df['magnitude'].max(), 2)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Earthquakes",
        total_eq
    )

    col2.metric(
        "Average Magnitude",
        avg_mag
    )

    col3.metric(
        "Maximum Magnitude",
        max_mag
    )

    style_metric_cards()

# =====================================================
# LIVE DATA
# =====================================================

elif menu == "Live Data":

    st.title("📡 Real-Time Earthquake Data")

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# PREDICTION
# =====================================================

elif menu == "Prediction":

    st.title("🔮 Earthquake Magnitude Prediction")

    st.image(
        "https://images.unsplash.com/photo-1581090700227-1e8e8b0f3f6f",
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        latitude = st.number_input(
            "Latitude",
            value=19.07
        )

    with col2:
        longitude = st.number_input(
            "Longitude",
            value=72.87
        )

    with col3:
        depth = st.number_input(
            "Depth",
            value=10.0
        )

    if st.button("Predict Magnitude"):

        input_data = pd.DataFrame({
            'latitude': [latitude],
            'longitude': [longitude],
            'depth': [depth]
        })

        prediction = model.predict(input_data)

        magnitude = prediction[0]

        st.success(
            f"Predicted Magnitude: {magnitude:.2f}"
        )

        st.progress(
            min(int(magnitude * 10), 100)
        )

        if magnitude < 3:

            st.success("🟢 Low Risk Earthquake")

        elif magnitude < 5:

            st.warning("🟡 Moderate Risk Earthquake")

        elif magnitude < 7:

            st.error("🟠 Dangerous Earthquake")

            send_email_alert(
                f"Dangerous Earthquake Detected! Magnitude: {magnitude:.2f}"
            )

        else:

            st.error("🔴 Extreme Earthquake")

            send_email_alert(
                f"Extreme Earthquake Alert! Magnitude: {magnitude:.2f}"
            )

            st.toast(
                "⚠️ Emergency Earthquake Alert!",
                icon="🚨"
            )

# =====================================================
# VISUALIZATION
# =====================================================

elif menu == "Visualization":

    st.title("📊 Earthquake Visualizations")

    st.subheader("Depth vs Magnitude")

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    ax1.scatter(
        df['depth'],
        df['magnitude']
    )

    ax1.set_xlabel("Depth")

    ax1.set_ylabel("Magnitude")

    ax1.set_title("Depth vs Magnitude")

    st.pyplot(fig1)

    st.subheader("Magnitude Distribution")

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    ax2.hist(
        df['magnitude'],
        bins=20
    )

    ax2.set_xlabel("Magnitude")

    ax2.set_ylabel("Frequency")

    st.pyplot(fig2)

    st.subheader("Earthquake Risk Distribution")

    low = len(df[df['magnitude'] < 3])

    medium = len(
        df[
            (df['magnitude'] >= 3) &
            (df['magnitude'] < 5)
        ]
    )

    high = len(df[df['magnitude'] >= 5])

    labels = ["Low", "Medium", "High"]

    values = [low, medium, high]

    fig3, ax3 = plt.subplots()

    ax3.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    st.pyplot(fig3)

    st.subheader("Earthquake Magnitude Trend")

    st.line_chart(df['magnitude'])

    st.subheader("Top 10 Magnitudes")

    top10 = df.nlargest(10, 'magnitude')

    st.bar_chart(top10['magnitude'])

# =====================================================
# LIVE MAP
# =====================================================

elif menu == "Live Map":

    st.title("🗺️ Live Earthquake Map")

    earthquake_map = folium.Map(
        location=[20, 78],
        zoom_start=2
    )

    for index, row in df.iterrows():

        magnitude = row['magnitude']

        if magnitude < 3:
            color = "green"

        elif magnitude < 5:
            color = "orange"

        else:
            color = "red"

        folium.CircleMarker(
            location=[
                row['latitude'],
                row['longitude']
            ],

            radius=max(magnitude * 2, 3),

            popup=f"""
            <b>Place:</b> {row['place']}<br>
            <b>Magnitude:</b> {magnitude}<br>
            <b>Depth:</b> {row['depth']}
            """,

            color=color,
            fill=True,
            fill_color=color

        ).add_to(earthquake_map)

    folium_static(
        earthquake_map,
        width=1200,
        height=600
    )

# =====================================================
# HEATMAP
# =====================================================

elif menu == "Heatmap":

    st.title("🔥 Earthquake Heatmap")

    heat_map = folium.Map(
        location=[20, 78],
        zoom_start=2
    )

    heat_data = df[
        ['latitude', 'longitude', 'magnitude']
    ].values.tolist()

    HeatMap(
        heat_data,
        radius=18,
        blur=15
    ).add_to(heat_map)

    folium_static(
        heat_map,
        width=1200,
        height=600
    )

# =====================================================
# AI ANOMALY DETECTION
# =====================================================

elif menu == "AI Anomaly Detection":

    st.title("🤖 AI Seismic Anomaly Detection")

    anomalies = df[df['anomaly'] == -1]

    st.warning(
        f"Detected {len(anomalies)} unusual seismic activities"
    )

    st.dataframe(
        anomalies,
        use_container_width=True
    )

# =====================================================
# DASHBOARD ANALYTICS
# =====================================================

elif menu == "Dashboard Analytics":

    st.title("📈 Dashboard Analytics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Earthquakes",
        len(df)
    )

    col2.metric(
        "Average Magnitude",
        round(df['magnitude'].mean(), 2)
    )

    col3.metric(
        "Maximum Magnitude",
        round(df['magnitude'].max(), 2)
    )

    style_metric_cards()

    st.subheader("Top Dangerous Areas")

    dangerous = df.sort_values(
        by='magnitude',
        ascending=False
    )

    st.dataframe(
        dangerous[
            ['place', 'magnitude', 'depth']
        ].head(10),

        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
---
<center>

<h3>🌍 Earthquake Prediction System</h3>

AI + ML Based Real-Time Seismic Monitoring

Developed using:
Python | Streamlit | Machine Learning | USGS API

</center>
""", unsafe_allow_html=True)