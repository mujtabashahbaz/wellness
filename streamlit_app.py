import streamlit as st
import requests

# Set Django server URL
API_URL = "http://127.0.0.1:8000/api/wellness_logs/"

# Title
st.title("Health and Wellness Tracker")

# Function to fetch wellness logs
def get_wellness_logs():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

# Display logs
logs = get_wellness_logs()

if logs:
    st.header("Your Wellness Logs")
    for log in logs:
        st.subheader(f"{log['date']} - {log['activity']}")
        st.write(f"Duration: {log['duration']} mins")
        st.write(f"Calories burned: {log['calories_burned']}")
        st.write(f"Notes: {log['notes']}")
else:
    st.write("No logs found.")

# Form to add a new log (this can be expanded to post to the API)
st.header("Add New Wellness Log")
activity = st.text_input("Activity")
duration = st.number_input("Duration (minutes)", min_value=0)
calories_burned = st.number_input("Calories Burned", min_value=0.0)
notes = st.text_area("Notes")

if st.button("Submit"):
    # Placeholder for API POST request logic
    st.write("Form submitted. (API logic needs to be implemented)")
