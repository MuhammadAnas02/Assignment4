import streamlit as st
st.set_page_config(page_title="BMI Converter", layout="centered")
custom_css = """
<style>
body { background-color: #f0f2f6; }
.stButton button { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px; }
.stTextInput>div>input { border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.title("BMI Converter")
weight = st.number_input("Enter weight in kg", min_value=0.0, value=70.0, step=0.1)
height = st.number_input("Enter height in meters", min_value=0.0, value=1.75, step=0.01)
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write("Your BMI is", round(bmi, 2))
