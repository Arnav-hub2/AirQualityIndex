import pandas as pd
from sklearn.model_selection import train_test_split
import os

def load_and_split_data():

    data_path = os.path.join(os.path.dirname(__file__), "..", "dataset", "cleaned_aqi_dataset.csv")

    df = pd.read_csv(r"C:\Users\dell\OneDrive\Desktop\Practice\mlpipeline\AirQuality\Data\processed\raw\aqi.csv")
    print(df.head())
    X = df[['PM2.5','PM10','NO2','SO2','CO','O3','Temperature','Humidity','WindSpeed']]
    y = df['AQI']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test