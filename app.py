import streamlit as st
from src.prediction import AQI_Prediction

model = AQI_Prediction()

st.title("Air Quality Index Prediction System")

st.write("Enter pollution and weather values to predict AQI")

PM25 = st.number_input("PM2.5", min_value=0.0)
PM10 = st.number_input("PM10", min_value=0.0)
NO2 = st.number_input("NO2", min_value=0.0)
SO2 = st.number_input("SO2", min_value=0.0)
CO = st.number_input("CO", min_value=0.0)
O3 = st.number_input("O3", min_value=0.0)
Temperature = st.number_input("Temperature", min_value=0.0)
Humidity = st.number_input("Humidity", min_value=0.0)
WindSpeed = st.number_input("Wind Speed", min_value=0.0)

if st.button("Predict AQI"):

    result = model.prediction(
        PM25,
        PM10,
        NO2,
        SO2,
        CO,
        O3,
        Temperature,
        Humidity,
        WindSpeed
    )

    st.success(f"Predicted AQI: {result}")