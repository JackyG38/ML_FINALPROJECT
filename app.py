import streamlit as st
import joblib
import numpy as np

# Load the trained model
model_path = 'model1_c.pkl'
loaded_model = joblib.load(model_path)

# Title of the app
st.title("Agriculture Weather Prediction")

# Description of the app
st.write("""
    This application predicts the Temperature, Average Precipitation, 
    and Relative Humidity based on the minimum and maximum yield.
    Enter the minimum and maximum yield to get predictions.
""")

# Input fields for user interaction
min_yield = st.number_input("Enter Minimum Yield", min_value=0.0, format="%.2f")
max_yield = st.number_input("Enter Maximum Yield", min_value=0.0, format="%.2f")

# When the user clicks on the "Predict" button
if st.button('Predict'):
    # Prepare input data for prediction
    input_data = np.array([[min_yield, max_yield]])
    
    # Get predictions from the model
    prediction = loaded_model.predict(input_data)
    
    # Display predictions
    st.write(f"Predicted Temperature: {prediction[0, 0]:.2f} °C")
    st.write(f"Predicted Average Precipitation: {prediction[0, 1]:.2f} mm")
    st.write(f"Predicted Relative Humidity: {prediction[0, 2]:.2f} %")
