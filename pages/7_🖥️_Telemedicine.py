import streamlit as st
import datetime
import googleapiclient.discovery
from google.oauth2.credentials import Credentials

# Mock function to send a follow-up email
def send_follow_up_email(patient_email):
    # Implement your email sending logic here
    print(f"Follow-up email sent to {patient_email}")

# Streamlit app
def main():
    st.header("Patient-Doctor Google Meet Scheduler")

    # Get patient and doctor details
    patient_name = st.text_input("Patient Name")
    patient_email = st.text_input("Patient Email")
    doctor_name = st.text_input("Doctor Name")
    doctor_email = st.text_input("Doctor Email")

    # Schedule Google Meet
    meet_date = st.date_input("Select Meet Date")
    meet_time = st.time_input("Select Meet Time")
    meeting_datetime = datetime.datetime.combine(meet_date, meet_time)

    if st.button("Schedule Google Meet"):
        # Initialize Google Calendar API
        creds = Credentials.from_authorized_user_info('/Users/aditya/Downloads/client_secret_557869841131-vddd1co8tp4m5vq08mq7ea28fm0au73r.apps.googleusercontent.com (1).json', ['https://www.googleapis.com/auth/calendar'])  # Add your OAuth2 credentials here
        service = googleapiclient.discovery.build('calendar', 'v3', credentials=creds)

        event = {
            'summary': 'Patient-Doctor Meet',
            'start': {
                'dateTime': meeting_datetime.isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (meeting_datetime + datetime.timedelta(hours=1)).isoformat(),
                'timeZone': 'UTC',
            },
            'attendees': [
                {'email': patient_email},
                {'email': doctor_email},
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        st.success(f"Google Meet scheduled. Event ID: {event['id']}")

        # Schedule follow-up email
        follow_up_date = meeting_datetime + datetime.timedelta(days=3)
        send_follow_up_email_button = st.button("Schedule Follow-Up Email")
        if send_follow_up_email_button:
            send_follow_up_email(patient_email)
            st.success("Follow-up email scheduled.")

if __name__ == "__main__":
    main()
