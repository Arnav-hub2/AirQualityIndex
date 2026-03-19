from datapreprocessing import load_and_split_data
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

output_dir = os.path.join(os.path.dirname(__file__), "..", "data1", "processed")
os.makedirs(output_dir, exist_ok=True)

X_train, X_test, y_train, y_test = load_and_split_data()

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

X_train_scaled.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
X_test_scaled.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
pd.DataFrame(y_train).to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
pd.DataFrame(y_test).to_csv(os.path.join(output_dir, "y_test.csv"), index=False)

artifacts_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts")
os.makedirs(artifacts_dir, exist_ok=True)

with open(os.path.join(artifacts_dir, "scaler.pkl"), "wb") as f:
    pickle.dump(scaler, f)

print("Scaling completed and files saved.")