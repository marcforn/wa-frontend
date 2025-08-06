import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def page_one():
    st.title("Page One")
    if st.button("Click me on Page One"):
        print("Button on Page One clicked!")
        st.success("Button on Page One clicked!")

def print_notifications_static():
    notifications_url = os.getenv("NOTIFICATIONS_URL")
    if not notifications_url:
        raise EnvironmentError("NOTIFICATIONS_URL environment variable is not set.")

    st.write(f"Notifications URL: {notifications_url}")
    try:
        response = requests.get(notifications_url)
        if response.status_code == 200:
            st.write("Notifications / endpoint result:")
            st.json(response.json())
        else:
            st.error(f"Failed to fetch /static: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error connecting to notifications service: {e}")

# Add a "Notifications" page to the Streamlit app
def notifications_page():
    st.title("Notifications Service Status")
    print_notifications_static()
        

def page_two():
    st.title("Page Two")
    if st.button("Click me on Page Two"):
        st.success("Button on Page Two clicked!")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Page One", "Page Two", "Notifications"))

    if page == "Page One":
        page_one()
    elif page == "Page Two":
        page_two()
    elif page == "Notifications":
        notifications_page()


if __name__ == "__main__":
    main() 