import streamlit as st
import plotly.express as px  # Placeholder for actual plotting library
from backend import get_data

# Add title and input widgets
st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select number of days to forecast (1-5)")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} forecast for next {days} days in {place}")

try:
    if place:
        # Get temperature/sky data for plotting
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Placeholder for actual figure creation logic
            figure = px.line(x=dates, y=temperatures, labels={
                "x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)  # Placeholder for actual plotting function

        # Get sky condition images
        if option == "Sky":
            # Map sky conditions to image paths
            images = {"Clear": "D:\\images\\clear.png",
                      "Clouds": "D:\\images\\cloud.png",
                      "Rain": "D:\\images\\rain.png",
                      "Snow": "D:\\images\\snow.png"}
            # Extract sky conditions from data
            sky_conditions = [dict["weather"][0]["main"]
                              for dict in filtered_data]
            # Map sky conditions to images
            image_paths = [images[condition] for condition in sky_conditions]
            # Display images in Streamlit
            st.image(image_paths, width=115)
except KeyError:
    st.error("Place not found. Please enter a valid place name.")
