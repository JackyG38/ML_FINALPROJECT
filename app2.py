import streamlit as st
import pandas as pd
import joblib

# Load your SARIMAX model
model_2 = joblib.load('sarimax_model.pkl')  

# Streamlit application layout for Model 2
st.title("Next Hour: Humidity in Your Greenhouse")

# Input fields for Model 2
date = st.date_input("Date:")
time = st.time_input("Time:")
temperature_ts = st.number_input("Temperature (°C):", min_value=-50.0, max_value=50.0, step=0.1)

# Extract the hour from the time input
time_of_day = time.hour

# Button to trigger prediction
if st.button("Predict Relative Humidity for the next hour"):
    try:
        # Combine date and time into a single datetime object
        datetime_input = pd.to_datetime(f"{date} {time}")

        # Prepare exogenous variables (e.g., temperature and time of day)
        exog_data = pd.DataFrame({
            'Temperature': [temperature_ts],  # Only one time step
            'Time_of_Day': [time_of_day],  # Current hour
        })

        # Check if the model expects a placeholder for Relative Humidity
        if 'Relative_Humidity' in model_2.data.param_names:  # Assuming model expects it
            exog_data['Relative_Humidity'] = 0.0  # Use a placeholder value

        # Make prediction for the next hour
        prediction_2 = model_2.predict(start=0, end=0, exog=exog_data)

        # Display the prediction rounded to 2 decimal places
        st.write(f"Predicted Relative Humidity for the next hour: {prediction_2[0]:.2f}%")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
