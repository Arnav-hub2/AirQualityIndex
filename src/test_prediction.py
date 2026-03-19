from prediction import AQI_Prediction

model = AQI_Prediction()

result = model.prediction(
    85,   # PM2.5
    120,  # PM10
    40,   # NO2
    20,   # SO2
    0.8,  # CO
    30,   # O3
    32,   # Temperature
    65,   # Humidity
    8     # WindSpeed
)

print("Predicted AQI:", result)