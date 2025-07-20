import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    # Sample dataset - replace with actual CSV read
    df = pd.DataFrame({
        'year': np.random.randint(2000, 2023, 100),
        'km_driven': np.random.randint(10000, 200000, 100),
        'fuel': np.random.choice(['Petrol', 'Diesel', 'CNG'], 100),
        'seller_type': np.random.choice(['Dealer', 'Individual'], 100),
        'transmission': np.random.choice(['Manual', 'Automatic'], 100),
        'price': np.random.randint(100000, 1000000, 100)
    })
    return df

@st.cache_resource
def train_model(df):
    df_encoded = df.copy()
    for col in ['fuel', 'seller_type', 'transmission']:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df[col])

    X = df_encoded.drop('price', axis=1)
    y = df_encoded['price']
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def main():
    st.title("🚗 Car Price Estimator")
    df = load_data()
    model = train_model(df)

    st.sidebar.header("Enter Car Details")
    year = st.sidebar.slider('Year of Purchase', 2000, 2022, 2015)
    km_driven = st.sidebar.number_input('Kilometers Driven', min_value=0, value=50000)
    fuel = st.sidebar.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.sidebar.selectbox('Seller Type', ['Dealer', 'Individual'])
    transmission = st.sidebar.selectbox('Transmission', ['Manual', 'Automatic'])

    input_df = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission]
    })

    for col in ['fuel', 'seller_type', 'transmission']:
        le = LabelEncoder()
        le.fit(df[col])
        input_df[col] = le.transform(input_df[col])

    if st.button('Predict Price'):
        prediction = model.predict(input_df)
        st.success(f"Estimated Car Price: ₹{int(prediction[0]):,}")

        st.subheader("Feature Importance")
        feat_imp = model.feature_importances_
        feat_names = input_df.columns
        fig, ax = plt.subplots()
        ax.barh(feat_names, feat_imp, color='skyblue')
        st.pyplot(fig)

if __name__ == "__main__":
    main()
