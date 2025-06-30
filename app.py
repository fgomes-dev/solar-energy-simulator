import streamlit as st
import requests
import matplotlib.pyplot as plt

# Constants
API_KEY = "mBPeRak1WlLZKJkQ9fGxWxYaJ45WYHSunl63GWPN"
API_URL = "https://developer.nrel.gov/api/pvwatts/v6.json"
DEFAULT_LAT = 34.0195
DEFAULT_LON = -118.4912
DEFAULT_COST_PER_KWH = 0.20

# Sidebar inputs
st.sidebar.title("📍 Location & System Settings")
lat = st.sidebar.number_input("Latitude", value=DEFAULT_LAT)
lon = st.sidebar.number_input("Longitude", value=DEFAULT_LON)
capacity = st.sidebar.slider("System Capacity (kW)", 0.5, 10.0, 1.0)
tilt = st.sidebar.slider("Tilt Angle (°)", 0, 45, 20)
azimuth = st.sidebar.slider("Azimuth (°)", 0, 360, 180)
cost_per_kwh = st.sidebar.number_input("Cost per kWh ($)", value=DEFAULT_COST_PER_KWH)

# Request parameters
params = {
    'api_key': API_KEY,
    'lat': lat,
    'lon': lon,
    'system_capacity': capacity,
    'azimuth': azimuth,
    'tilt': tilt,
    'array_type': 1,
    'module_type': 1,
    'losses': 14
}

# API call
st.title("🔆 Solar Energy Output Simulator")
st.write("Estimates monthly energy production and cost savings for your solar system.")
response = requests.get(API_URL, params=params)
data = response.json()

if "outputs" in data:
    monthly_output = data['outputs']['ac_monthly']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    savings = [round(kwh * cost_per_kwh, 2) for kwh in monthly_output]
    
    st.subheader("📊 Estimated Monthly Output (kWh)")
    st.bar_chart(monthly_output)
    
    st.subheader("💰 Estimated Monthly Savings ($)")
    st.bar_chart(savings)
    
    total_output = sum(monthly_output)
    total_savings = sum(savings)
    st.success(f"**Total Yearly Output**: {total_output:.2f} kWh")
    st.success(f"**Estimated Annual Savings**: ${total_savings:.2f}")
else:
    st.error("Failed to fetch data. Check your API key or parameters.")
