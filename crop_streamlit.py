import streamlit as st
import pandas as pd
import joblib 

st.title("CROP PREDICTION ANALYSIS")

# Input fields for user data
item_code = st.number_input('Enter Item Code (CPC)', min_value=0)
area_harvested = st.number_input('Enter the Area Harvested (in Hectares)', min_value=0.0)
yield_value = st.number_input('Enter the Yield Value (in kg/ha)', min_value=0.0)
producing_animals_slaughtered_value = st.number_input('Enter the Producing Animals/Slaughtered Value', min_value=0.0)
laying_value = st.number_input('Enter the Laying Value', min_value=0.0)
yield_carcass_weight_value = st.number_input('Enter the Yield/Carcass Weight Value', min_value=0.0)
milk_animals_value = st.number_input('Enter the Milk Animals Value', min_value=0.0)

# Load the trained model
model = joblib.load(r"D:\1 DS PROJECTS\Crop prediction\model.pkl")

# Predict button
if st.button('Predict Production'):
    # Prepare the input data for prediction
    input_data = pd.DataFrame([[
        item_code,
        area_harvested,
        yield_value,
        producing_animals_slaughtered_value,
        laying_value,
        yield_carcass_weight_value,
        milk_animals_value
    ]], columns=[
        'Item Code (CPC)',
        'Area_Harvested_in_Hectares',
        'Yield_Value in kg/ha',
        'Producing Animals/Slaughtered_Value',
        'Laying_Value',
        'Yield/Carcass Weight_Value',
        'Milk Animals_Value'
    ])

    # Make the prediction
    production = model.predict(input_data)[0]

    # Display the result


    st.write(f"Predicted Production: {production.round(2)} units")
st.header("REFERENCE TABLE")
df=pd.read_csv('cleansed_crop_data.csv')
st.dataframe(df)
