import streamlit as st
import pandas as pd
import joblib

# Load your Model 2
model_2 = joblib.load('sarimax_model.pkl')

# Streamlit application layout for Model 2
st.title("Next 2 Hours: Humidity in Your Greenhouse")

# Input fields for Model 2
date = st.date_input("Date:")
time = st.time_input("Time:")
temperature_ts = st.number_input("Temperature:", min_value=-50.0, max_value=50.0, step=0.1)  # Fix the input type

# Extract the hour from the time input
time_of_day = time.hour  # Directly access the hour attribute

# Placeholder for the third input (Relative_Humidity)
# Since we're predicting Relative Humidity, we can use a placeholder value like 0 or any default value
# This will allow the model to work with the expected 3 inputs (Temperature, Time_of_Day, Relative_Humidity)
placeholder_relative_humidity = 0.0  # Or any default value that makes sense for your model

if st.button("Predict Relative Humidity for next 2 hours"):
    try:
        # Combine date and time into a single datetime object (not used in prediction, just for reference)
        datetime_input = pd.to_datetime(f"{date} {time}")

        # Create a DataFrame for exogenous variables (temperature, time of day, and placeholder relative humidity)
        exog_row = pd.DataFrame({
            'Temperature': [temperature_ts],
            'Time_of_Day': [time_of_day],
            'Relative_Humidity': [placeholder_relative_humidity]  # Add placeholder for relative humidity
        })

        # Extend to match the required shape (3418, 3)
        exog_data = pd.concat([exog_row] * 3418, ignore_index=True)

        # Ensure the exogenous variables have the correct shape
        st.write(f"Exogenous Data Shape: {exog_data.shape}")

        # Make prediction (ensure the model expects these features and this format)
        prediction_2 = model_2.predict(start=datetime_input, end=datetime_input, exog=exog_data)

        # Display the prediction result rounded to 2 decimal places
        st.write(f"Predicted Relative Humidity for the next 2 hours: {prediction_2[0]:.2f}%")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
