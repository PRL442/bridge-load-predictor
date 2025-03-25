import streamlit as st
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

# Load model and preprocessing pipeline
model = tf.keras.models.load_model("tf_bridge_model.keras")
preprocessor = joblib.load("preprocessing_pipeline.pkl")

# Page title
st.title("Bridge Load Predictor")
st.markdown("🔩 Enter bridge specifications below to estimate its maximum load capacity (in tons).")

# User input
span = st.slider("Span (ft)", min_value=100.0, max_value=599.0, value=350.0)
deck_width = st.slider("Deck Width (ft)", min_value=20.0, max_value=60.0, value=40.0)
age = st.slider("Age (years)", min_value=1, max_value=100, value=50)
lanes = st.slider("Number of Lanes", min_value=1, max_value=6, value=4, step=1)
material = st.selectbox("Material", ["Steel", "Concrete", "Composite"])
condition = st.slider("Condition Rating (1 = Poor, 5 = Excellent)", min_value=1, max_value=5, value=3)

# Create input DataFrame
input_data = pd.DataFrame({
    "Span_ft": [span],
    "Deck_Width_ft": [deck_width],
    "Age_Years": [age],
    "Num_Lanes": [lanes],
    "Material": [material],
    "Condition_Rating": [condition]
})

# Predict
if st.button("Predict Max Load"):
    processed_input = preprocessor.transform(input_data)
    prediction = model.predict(processed_input)
    st.success(f"Estimated Max Load Capacity: **{prediction[0][0]:.2f} tons**")