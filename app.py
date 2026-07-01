import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}
.stButton>button{
    width:100%;
    background-color:#4CAF50;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:3em;
}
.stButton>button:hover{
    background-color:#45a049;
}
.result{
    padding:20px;
    border-radius:12px;
    background:#e8f5e9;
    color:#1b5e20;
    font-size:24px;
    font-weight:bold;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------------------
# Header
# -------------------------------
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to estimate its price.")

st.divider()

# -------------------------------
# Input Fields
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sq.ft)",
        min_value=100,
        max_value=10000,
        value=1000,
        step=50
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=2
    )

with col2:
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

st.divider()

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price 💰"):

    input_data = np.array([[area, bedrooms, bathrooms]])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="result">
        Estimated House Price<br><br>
        ₹ {prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
