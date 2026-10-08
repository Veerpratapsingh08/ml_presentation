import streamlit as st
import pandas as pd
import joblib

model = joblib.load("carbon_model.pkl")

st.title("Carbon Price Prediction")
st.write(
    "Enter the details of the carbon pricing initiative to forecast the price for the next year."
)

st.divider()


instrument_type = st.selectbox(
    "Instrument Type",
    ['Carbon tax', 'ETS']
)

region = st.selectbox(
    "Region",
    ['Europe & Central Asia', 'East Asia & Pacific', 'Middle East & North Africa', 
     'North America', 'Latin America & Caribbean', 'Sub-Saharan Africa']
)

income_group = st.selectbox(
    "Income Group",
    ['High income', 'Upper middle income', 'Upper middle ']
)


year = st.number_input(
    "Current Year",
    min_value=1990,
    max_value=2100,
    value=2024,
    step=1
)

price = st.number_input(
    "Current Price (US$/tCO2e)",
    min_value=0.0,
    max_value=500.0,
    value=10.0,
    step=0.1
)

if st.button("Predict Next Year Price"):


    initiative = pd.DataFrame({
        "Instrument_Type": [instrument_type],
        "Region": [region],
        "Income_group": [income_group],
        "Year": [year],
        "Price": [price]
    })

    prediction = model.predict(initiative)
    
    st.divider()
    
    st.success(f"Predicted Next Year Price: ${prediction[0]:.2f} US$/tCO2e")
