import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itinerary")
st.write("Plan your day trip  itenerary by entering your city and interests")

with st.form('Planner _form'):
    city=st.text_input('Enter the city name for your trip ')
    interests = st.text_input("please enter interests in comma seperated format")
    submiited = st.form_submit_button("Generate itinerary")

    if submiited:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_itinerary()
            
            st.subheader("Your Itinerary: ")
            st.markdown(itinerary)
    else:
        st.warning("Please fill all the details to generate the itienraray") 

