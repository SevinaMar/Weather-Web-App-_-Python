import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1,max_value=5,
                 help="Select the number of forecasted days")
option =  st.selectbox("Select data to view", ("Temperature","Sky Condition"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/sky data
        forecast_data = get_data(place,days)

        if option == 'Temperature':
            temperatures = [temp['main']['temp'] / 10 for temp in forecast_data]
            dates = [temp['dt_txt'] for temp in forecast_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={'w':'Date','y':'Temerature'})
            st.plotly_chart(figure)
        if option == 'Sky Condition':
            sky_condition = [temp['weather'][0]['main'] for temp in forecast_data]
            sky = {'Clear':'images/clear.png' ,'Clouds':'images/cloud.png',
                   'Rain':'images/rain.png' , 'Snow':'images/snow.png'}
            img_paths = [sky[condition] for condition in sky_condition]
            st.image(img_paths, width=85)
    except KeyError:
        st.info("Please enter a correct name of a city")