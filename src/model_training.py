import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

base_dir = os.path.dirname(__file__)

data_path = os.path.join(base_dir, "..", "data1", "processed")
artifact_path = os.path.join(base_dir, "..", "artifacts")

os.makedirs(artifact_path, exist_ok=True)

X_train = pd.read_csv(os.path.join(data_path, "X_train.csv"))
X_test = pd.read_csv(os.path.join(data_path, "X_test.csv"))
y_train = pd.read_csv(os.path.join(data_path, "y_train.csv"))
y_test = pd.read_csv(os.path.join(data_path, "y_test.csv"))

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("Model trained successfully")
print("R2 Score:", r2)
print("Mean Squared Error:", mse)

model_path = os.path.join(artifact_path, "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Model saved in artifacts folder")