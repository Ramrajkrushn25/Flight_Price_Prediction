# Flight Price Prediction 🛫

This project focuses on predicting flight ticket prices based on various features such as stops, departure time, duration, and more. Using machine learning techniques, the model analyzes historical data to predict prices with high accuracy, aiding travelers and businesses in making informed decisions.

---

## Features 📊

The dataset includes the following features used for prediction:

- **Total_Stops**: Number of stops during the flight.
- **day**: Day of the month the flight is scheduled.
- **month**: Month of the year the flight is scheduled.
- **Dep_hour**: Hour of flight departure.
- **Dep_min**: Minute of flight departure.
- **Arrival_hour**: Hour of flight arrival.
- **Arrival_min**: Minute of flight arrival.
- **Duration_hours**: Total flight duration in hours.
- **Duration_minutes**: Total flight duration in minutes.
- **airlines**: The airline operating the flight .
- **source**: Source city or airport of the flight.
- **destination**: Destination city or airport of the flight.
- **Price (target)**: The price of the flight ticket (dependent variable).

---

## Objective 🎯

The primary goal of this project is to build a regression model that accurately predicts flight ticket prices based on the given features. This model can help:
- Travelers plan budgets by estimating flight costs.
- Airlines analyze pricing strategies.
- Travel agencies automate price predictions for customer queries.

---

## Data Preprocessing 🛠️

The dataset requires the following preprocessing steps:
1. **Handling Missing Values**: Filling null values and dropping rows with duplicated data.
2. **Feature Engineering**: 
   - Extracting `day`, `month`, `Dep_hour`, `Dep_min`, `Arrival_hour`, and `Arrival_min` from datetime fields.
   - Converting `Total_Stops` into numeric values.
   - Encoding categorical columns (`airlines`, `source`, `destination`) using techniques like one-hot encoding.
3. **Scaling**: Normalizing numerical columns.
4. **Splitting Data**: Dividing the dataset into training and testing sets for model evaluation.

---
## Results 📈

The best-performing model achieved:
- **R² Score:** 0.83
