import streamlit as st


st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select number of days to forecast (1-5)")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} forecast for next {days} days in {place}")
