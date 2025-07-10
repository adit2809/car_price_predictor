import streamlit as st
import pandas as pd
import pickle

# Load the model and data columns
model = pickle.load(open('car_model.pkl', 'rb'))
data_columns = pickle.load(open('columns.pkl', 'rb'))  # contains column names used in training

st.title("🚗 Car Price Predictor")

# Inputs from user
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2015)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
fuel_type = st.selectbox("Fuel Type", options=['Petrol', 'Diesel', 'CNG'])
company = st.selectbox("Company", options=[col.replace("company_", "") for col in data_columns if "company_" in col])

# Predict button
if st.button("Predict Price"):
    # Build input row
    input_dict = {
        'year': year,
        'kms_driven': kms_driven,
    }

    for col in data_columns:
        if col.startswith("fuel_type_"):
            input_dict[col] = 1 if col == f"fuel_type_{fuel_type}" else 0
        elif col.startswith("company_"):
            input_dict[col] = 1 if col == f"company_{company}" else 0
        elif col not in ['year', 'kms_driven']:
            input_dict[col] = 0  # default for other one-hot columns

    input_df = pd.DataFrame([input_dict])
    price = model.predict(input_df)[0]

    st.success(f"Estimated Price: ₹{int(price):,}")
