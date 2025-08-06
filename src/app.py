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
        

def page_two():
    st.title("Page Two")
    if st.button("Click me on Page Two"):
        st.success("Button on Page Two clicked!")

def notifications_page():
    st.title("Notifications Service")
    
    # Configuration for the notifications service from environment variable
    NOTIFICATIONS_URL = os.getenv("NOTIFICATIONS_URL")
    
    # Check if environment variable is set
    if not NOTIFICATIONS_URL:
        st.error("❌ NOTIFICATIONS_URL environment variable is not set!")
        st.info("Please create a .env file with NOTIFICATIONS_URL")
        st.code("NOTIFICATIONS_URL=http://localhost:8000", language="bash")
        return
    
    # Display the current configuration
    st.subheader("Configuration")
    st.info(f"🔗 Connecting to: {NOTIFICATIONS_URL}")
    
    # Health check
    st.subheader("Service Health")
    try:
        health_response = requests.get(f"{NOTIFICATIONS_URL}/health", timeout=5)
        if health_response.status_code == 200:
            health_data = health_response.json()
            st.success(f"✅ Service Status: {health_data['status']}")
        else:
            st.error(f"❌ Service Health Check Failed: {health_response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Cannot connect to notifications service: {str(e)}")
        st.info("Make sure the notifications service is running on the configured URL")
        return
    
    # Get timestamp data
    st.subheader("Timestamp from Notifications Service")
    try:
        date_response = requests.get(f"{NOTIFICATIONS_URL}/date", timeout=5)
        if date_response.status_code == 200:
            date_data = date_response.json()
            
            # Display the raw data
            st.json(date_data)
            
            # Display formatted information
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Date", date_data["date"])
            
            with col2:
                # Convert timestamp to readable format
                timestamp = date_data["timestamp"]
                readable_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                st.metric("Timestamp", readable_time)
            
            with col3:
                st.metric("Timezone", date_data["timezone"])
            
            # Display additional information
            st.subheader("Additional Information")
            st.write(f"**Raw Timestamp:** {timestamp}")
            st.write(f"**Unix Timestamp:** {int(timestamp)}")
            
        else:
            st.error(f"❌ Failed to get date data: {date_response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching timestamp: {str(e)}")
    
    # Display scheduled tasks
    st.subheader("Scheduled Tasks")
    try:
        tasks_response = requests.get(f"{NOTIFICATIONS_URL}/tasks", timeout=5)
        if tasks_response.status_code == 200:
            tasks_data = tasks_response.json()
            if tasks_data:
                for task in tasks_data:
                    with st.expander(f"Task: {task['id']}"):
                        st.write(f"**Function:** {task['func_name']}")
                        st.write(f"**Trigger:** {task['trigger']}")
                        st.write(f"**Next Run:** {task['next_run_time'] or 'Not scheduled'}")
            else:
                st.info("No scheduled tasks found")
        else:
            st.error(f"❌ Failed to get tasks: {tasks_response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching tasks: {str(e)}")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Page One", "Page Two", "Notifications"))

    if page == "Page One":
        page_one()
    elif page == "Page Two":
        page_two()
    else:
        notifications_page()

if __name__ == "__main__":
    main() 