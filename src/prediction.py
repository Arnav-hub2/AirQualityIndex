import os
import pickle
import numpy as np

class AQI_Prediction:

    def __init__(self):

        base_dir = os.path.dirname(__file__)
        artifacts_dir = os.path.normpath(os.path.join(base_dir, "..", "artifacts"))

        scaler_path = os.path.join(artifacts_dir, "scaler.pkl")
        model_path = os.path.join(artifacts_dir, "model.pkl")

        if not os.path.exists(scaler_path) or not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Artifacts not found in {artifacts_dir}. Expected scaler.pkl and model.pkl"
            )

        with open(scaler_path, "rb") as f:
            self.scaler = pickle.load(f)

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def prediction(self, PM25, PM10, NO2, SO2, CO, O3, Temperature, Humidity, WindSpeed):

        input_data = np.array([[PM25, PM10, NO2, SO2, CO, O3, Temperature, Humidity, WindSpeed]])

        scaled_input = self.scaler.transform(input_data)

        result = self.model.predict(scaled_input)

        return result[0]