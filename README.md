# 🌿 Climate Intelligence

## Heatwave Monitoring, Prediction & Early Warning System

A Streamlit-based Climate Intelligence dashboard designed to monitor environmental conditions, assess heatwave risk, visualize climate trends, and provide early warning information.

This project was developed as a functional prototype for an **OOSE (Object-Oriented Software Engineering)** use case, focusing on the functional requirement of **Heatwave Prediction and Early Warning**.

---

## 📌 Project Overview

Heatwaves are becoming an important environmental and public health concern. Early identification of high-risk conditions can help support monitoring and decision-making.

The **Climate Intelligence** system provides an interactive dashboard that analyzes environmental parameters such as:

- Temperature
- Humidity
- Heat Index
- Wind Speed

The system calculates a composite heatwave risk score and classifies the risk into different levels.

The dashboard also provides historical analysis, predictive analytics, climate risk maps, explainable risk factors, scenario simulation, and an alert center.

---

## 🎯 Objectives

- Monitor important environmental conditions.
- Calculate heatwave risk using a rule-based risk engine.
- Classify climate conditions into different risk levels.
- Provide early heatwave warning information.
- Visualize climate trends using interactive graphs.
- Compare heatwave risk across different cities.
- Analyze historical climate patterns.
- Provide scenario-based "What-If" analysis.
- Explain the factors contributing to the calculated risk.

---

## ✨ Features

### 🏠 Command Center

The main dashboard provides an overall view of the selected location.

It displays:

- Current Temperature
- Humidity
- Heat Index
- Wind Speed
- Composite Risk Score
- Current Risk Level
- India Climate Risk Map
- Recent Risk Trend
- Long-Term Temperature Trend
- Humidity Trend
- City Risk Comparison
- Early Heatwave Warning

---

### 🔮 Predictive Analytics

Provides a simulated 7-day climate risk forecast.

It includes:

- Expected temperature
- Humidity
- Heat Index
- Heatwave probability
- Risk level
- High-risk day count
- Temperature forecast graph
- Heatwave probability graph

---

### 📈 Historical Intelligence

Provides historical climate analysis using simulated climate data.

It includes:

- Average temperature
- Maximum temperature
- Minimum temperature
- Temperature evolution from 2020–2026
- Annual average temperature
- Seasonal temperature patterns

---

### 🗺️ Climate Risk Map

Provides a geographical visualization of climate risk across selected Indian cities.

The map displays:

- City location
- Temperature
- Humidity
- Heat Index
- Risk Score
- Risk Level

A regional Maharashtra view is also included.

---

### 🧠 Explainable AI

Provides an interpretable breakdown of factors contributing to climate risk.

The dashboard visualizes factors such as:

- Temperature
- Humidity
- Heat Index
- Historical Anomaly
- Recent Trend

This helps users understand why a particular risk level has been generated.

---

### 🧪 What-If Simulator

Allows users to modify environmental conditions and observe how the heatwave risk changes.

Users can adjust:

- Temperature
- Humidity
- Wind Speed

The system then calculates:

- Simulated Risk Score
- Change from Current Risk
- Simulated Heat Index
- Simulated Risk Level
- Simulated Warning

---

### 🚨 Alert Center

Provides heatwave warning and alert information.

It displays:

- Current alert status
- Location
- Risk Score
- Heat Index
- Risk severity
- Recommended monitoring actions
- Alert history

---

## ⚙️ Risk Calculation

The system uses a **rule-based risk engine** to calculate a composite risk score between 0 and 100.

The calculation considers:

- Temperature
- Humidity
- Heat Index
- Wind Speed

The resulting score is classified as:

| Risk Score | Risk Level |
|------------|------------|
| 0–44 | LOW |
| 45–69 | MODERATE |
| 70–84 | HIGH |
| 85–100 | EXTREME |

Higher risk conditions can trigger an early heatwave warning.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Plotly**
- **HTML/CSS** for dashboard styling

---

## 📂 Project Structure

```text
Climate-Intelligence/
│
├── pracs.py
└── README.md
