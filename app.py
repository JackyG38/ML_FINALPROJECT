import streamlit as st
import joblib
import numpy as np

# Load the trained model
model_path = 'model1_c.pkl'  # Adjust path if needed
model = joblib.load(model_path)

# Title of the app
st.title("Predict Temperature, Precipitation, and Humidity Based on Yield")

# Instructions
st.write("""
    This app predicts the Temperature (°C), Average Precipitation (mm), and Relative Humidity (%) based on the minimum and maximum yield.
    Please enter the values below and click 'Predict' to see the results.
""")

# User inputs for minimum and maximum yield
yield_min = st.number_input("Enter Minimum Yield:", min_value=0.0, value=1000.0, step=100.0)
yield_max = st.number_input("Enter Maximum Yield:", min_value=0.0, value=3000.0, step=100.0)

# Prepare the input data
input_data = np.array([[yield_min, yield_max]])

# Button to make prediction
if st.button("Predict"):
    try:
        # Make the prediction
        prediction = model.predict(input_data)

        # Display the results
        st.subheader("Predicted Values")
        st.write(f"**Temperature**: {prediction[0, 0]:.2f} °C")
        st.write(f"**Average Precipitation**: {prediction[0, 1]:.2f} mm")
        st.write(f"**Relative Humidity**: {prediction[0, 2]:.2f} %")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Additional Information Section
st.markdown("""
    ### About the Model
    This model is trained using a **Random Forest Regressor** and it predicts three important environmental factors based on two features: minimum and maximum yield. These predictions help in managing greenhouse environments more efficiently.
    
    The model is built using the `RandomForestRegressor` from Scikit-learn and supports multi-output regression to predict multiple environmental factors simultaneously.
""")
