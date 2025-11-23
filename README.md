☁️ Weather Forecast Application (Streamlit/OpenWeatherMap)

A simple, interactive web application built with Streamlit to display the weather forecast for the next 1 to 5 days using the OpenWeatherMap API.

The application demonstrates strong software practices, including separation of concerns (backend/frontend) and robust error handling.

✨ Features

Interactive UI: Uses Streamlit widgets (text input, slider, selectbox) for user control.

Dynamic Visualization: Displays temperature data via an interactive Plotly line chart.

Visual Weather: Shows sky conditions (Clear, Clouds, Rain, Snow) using corresponding images.

Robust Error Handling: Safely handles cases where a city name is not found by the API (try...except KeyError).

Modular Design: Separates the backend API logic (backend.py) from the frontend application logic (main.py).

🛠️ Requirements

1. Requirements File (requirements.txt)

All necessary Python libraries for this project are listed in the requirements.txt file, ensuring environment reproducibility.

streamlit
requests
plotly
plotly-express
python-dotenv


2. Installation

You can install all required dependencies at once using pip:

pip install -r requirements.txt


⚙️ Setup and Configuration

1. Get an API Key (OpenWeatherMap)

You need a free API key from OpenWeatherMap to access the forecast data:

Register an account on OpenWeatherMap.

Generate an API key (it may take a few minutes to become active).

2. Configure Environment Variables (.env)

For security, the API key must be stored securely outside the main codebase using the python-dotenv library.

Create a file named .env in the root directory of your project.

Add your API key to this file in the following exact format:

API_KEY="YOUR_ACTUAL_OPENWEATHERMAP_API_KEY_HERE"


3. Image Assets

The application visualizes sky conditions using local images. You must ensure the necessary files exist at the specified paths (e.g., D:\images\clear.png).

▶️ How to Run the Application

Navigate to your project's root directory in the terminal and execute the following command:

streamlit run main.py


The application will open automatically in your web browser (usually at http://localhost:8501).

📂 Project Structure

File/Directory

Role and Description

main.py

Frontend (Streamlit): GUI, user input handling, conditional visualization logic, and primary error handling.

backend.py

Backend (API Logic): Handles loading the API_KEY, making the requests call, and filtering the raw data from OpenWeatherMap.

requirements.txt

Dependencies: Lists all necessary Python libraries.

.env

Configuration: Securely stores the API key.

images/

Assets: Directory containing the PNG files for weather visualization.