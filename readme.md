# Air Quality Index Prediction using Linear Regression

## Project Overview

Air pollution is a major environmental and public health problem across the world. Monitoring and predicting air quality helps governments, organizations, and citizens take preventive actions to reduce health risks.

This project focuses on predicting the **Air Quality Index (AQI)** using **Machine Learning (Linear Regression)**. The model uses pollution and weather-related parameters to estimate AQI levels and provide insights into environmental conditions.

---

# Why This Topic and Dataset Were Chosen

The **Air Quality Index dataset** was chosen because air pollution is a serious real-world problem affecting both **public health and the environment**.

The dataset includes important pollution indicators such as:

* PM2.5
* PM10
* NO₂
* SO₂
* CO
* O₃
* Weather conditions (Temperature, Humidity, Wind Speed)

These parameters directly influence air quality levels.

Since **AQI is a continuous numerical value**, regression models can effectively predict it. This prediction system can help **environmental agencies and smart city systems monitor pollution and take preventive measures.**

---

# Machine Learning Model Used

## Linear Regression

Linear Regression was chosen because:

* The **target variable (AQI)** is a **continuous numerical value**
* Pollution indicators and weather conditions have a **measurable relationship with AQI**
* It is a **simple, efficient, and interpretable model**
* Suitable for **predicting numerical environmental data**

---

# Features Used in the Model

The model uses environmental and weather-related parameters that influence air quality.

### 1. PM2.5

PM2.5 refers to fine particulate matter with a diameter of **2.5 micrometers or smaller**.
These particles can penetrate deep into the lungs and significantly affect air quality.

### 2. PM10

PM10 represents particulate matter with a diameter of **10 micrometers or smaller**.
Higher concentrations of PM10 contribute to poor air quality.

### 3. NO₂ (Nitrogen Dioxide)

NO₂ is mainly produced by **vehicle emissions and industrial processes**.
High levels increase air pollution and affect respiratory health.

### 4. SO₂ (Sulfur Dioxide)

SO₂ is released from **burning fossil fuels and industrial activities**.
It contributes to air pollution and acid rain.

### 5. CO (Carbon Monoxide)

CO is a harmful gas produced from **incomplete combustion of fuels** such as gasoline and coal.

### 6. O₃ (Ozone)

Ground-level ozone forms from **chemical reactions between pollutants and sunlight** and is harmful to human health.

### 7. Temperature

Temperature influences **chemical reactions in the atmosphere** and affects pollutant concentration levels.

### 8. Humidity

Humidity affects how pollutants **spread and concentrate in the air**.

### 9. Wind Speed

Wind speed influences how pollutants **disperse in the environment**. Higher wind speed often reduces pollution concentration.

---

# Business Value

### 1. Pollution Monitoring

Helps authorities monitor pollution trends and environmental conditions.

### 2. Early Warning System

Predicts AQI levels in advance and alerts people about dangerous pollution levels.

### 3. Environmental Decision Making

Supports government agencies in creating pollution control policies.

### 4. Public Health Protection

Helps people take preventive health measures when pollution levels are high.

### 5. Smart City Integration

Can be integrated into **smart city systems** for automated environmental monitoring.

---

# Target Customers / End Users

This system can be used by:

* Environmental Protection Agencies
* Government Pollution Control Boards
* Smart City Management Systems
* Weather Forecasting Organizations
* Public Health Departments
* Environmental Research Institutions

These organizations can use the system to **analyze pollution data, predict AQI levels, and take preventive actions to improve air quality.**

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Machine Learning (Linear Regression)

---

# Expected Output

The system predicts the **Air Quality Index (AQI)** based on pollution and weather parameters, helping users understand air quality conditions and potential risks.

---

# Future Improvements

* Use advanced models such as **Random Forest, Gradient Boosting, or Neural Networks**
* Integrate **real-time pollution data**
* Deploy the system as a **web application for public use**
* Add **visual dashboards for AQI monitoring**
