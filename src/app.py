import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
st.set_page_config(page_title="Wealth Assistant", page_icon="💼", layout="wide")

def fetch_notifications_health():
    notifications_service_url = os.getenv("NOTIFICATIONS_URL")
    if not notifications_service_url:
        raise EnvironmentError("NOTIFICATIONS_URL environment variable is not set.")

    url = f"{notifications_service_url.rstrip('/')}/health"
    st.write(f"Calling notifications endpoint: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            st.write("/health response:")
            st.json(response.json())
        else:
            st.error(f"Request failed: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error connecting to notifications service: {e}")


def notifications_page():
    st.header("Notifications")
    fetch_notifications_health()


def reits_page():
    st.header("REITs")
    fetch_reits_health()

def fetch_reits_health():
    reits_service_url = os.getenv("REITS_URL")
    if not reits_service_url:
        raise EnvironmentError("REITS_URL environment variable is not set.")

    url = f"{reits_service_url.rstrip('/')}/health"
    st.write(f"Calling REITs endpoint: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            st.write("/hello response:")
            st.json(response.json())
        else:
            st.error(f"Request failed: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error connecting to REITs service: {e}")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Notifications", "REITs"))

    st.title("Wealth Assistant 💼")

    if page == "Notifications":
        notifications_page()
    elif page == "REITs":
        reits_page()


if __name__ == "__main__":
    main() 