import streamlit as st
import streamlit_authenticator as stauth
from streamlit_calendar import calendar
import yaml
from yaml.loader import SafeLoader
import os
import pandas as pd
import numpy as np

# Define the initial configuration
initial_config = {
    "credentials": {
        "usernames": {
            "jsmith": {
                "email": "jsmith@gmail.com",
                "failed_login_attempts": 0,
                "logged_in": 0,
                "name": "John Smith",
                "password": "abc"
            },
            "rbriggs": {
                "email": "rbriggs@gmail.com",
                "failed_login_attempts": 0,
                "logged_in": 0,
                "name": "Rebecca Briggs",
                "password": "def"
            }
        }
    },
    "cookie": {
        "expiry_days": 30,
        "key": "some_signature_key",
        "name": "some_cookie_name"
    },
    "preauthorized": {
        "emails": [
        "melsby@gmail.com"
        ]
    }
}

calendar_options = {
    "editable": "false",
    "selectable": "false",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "01:00:00",
    "slotMaxTime": "25:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "field",
    "resources": [
        {"id": "a", "field": "feld1", "title": "feld1"},
        {"id": "b", "field": "feld1", "title": "feld2"},
        {"id": "c", "field": "feld1", "title": "feld3"},
        {"id": "d", "field": "feld1", "title": "feld4"},
        {"id": "e", "field": "feld1", "title": "feld5"},
        {"id": "f", "field": "feld1", "title": "feld6"},
    ],
}

calendar_events = [
    {
        "title": "123",
        "start": "2024-05-01T08:30:00",
        "end": "2024-05-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "423",
        "start": "2024-05-01T07:30:00",
        "end": "2024-05-01T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "521",
        "start": "2024-05-01T10:40:00",
        "end": "2024-05-01T12:30:00",
        "resourceId": "a",
    }
]

custom_css="""
   .fc-event-past {
        opacity: 0.8;
    }
   .fc-event-time {
        font-style: italic;
    }
   .fc-event-title {
        font-weight: 700;
    }
   .fc-toolbar-title {
        font-size: 2rem;
    }
"""

data = {
    'Time': pd.date_range(start='00:00', end='23:59', freq='H'),
    'Blood Pressure': np.random.randint(40, 220, size=24) # Random blood pressure values
}

df = pd.DataFrame(data)

# Path to the configuration file
config_path = 'config.yaml'
st.set_page_config(layout="wide")

# Check if the configuration file exists
if not os.path.exists(config_path):
    # Create the configuration file with the initial configuration
    with open(config_path, 'w') as file:
        yaml.dump(initial_config, file, Dumper=yaml.Dumper) # Corrected line

# Load configuration
with open(config_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
# Render the login widget
name, authentication_status, username = authenticator.login()

if 'register_form_open' not in st.session_state:
    st.session_state['register_form_open'] = False
if 'data_editor_open' not in st.session_state:
    st.session_state['data_editor_open'] = False

if st.session_state["authentication_status"] is not True:
    if st.button("Register") and st.session_state['register_form_open'] is not True:
        st.session_state['register_form_open'] = not st.session_state['register_form_open']

# Button to toggle the data editor

# Registration form
if st.session_state['register_form_open'] and st.session_state["authentication_status"] is not True:
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            config['credentials']['usernames'][username_of_registered_user or "default"] = {
                "email": email_of_registered_user or "default",
                "failed_login_attempts": 0,
                "logged_in": 0,
                "name": name_of_registered_user or "default",
                "password": "your_password_here" # You should handle password securely, it doesn't get returned ^^??
            }
            # Write the updated config back to the file
            with open(config_path, 'w') as file:
                yaml.dump(config, file, Dumper=yaml.Dumper)
            st.session_state['register_form_open'] = False
    except Exception as e:
        st.error(e)

# Data editor

# Handle authentication status
if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    if st.button("Edit"):
        st.session_state['data_editor_open'] = not st.session_state['data_editor_open']
    if st.session_state['data_editor_open']:
        st.data_editor(initial_config)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.line_chart(df.set_index('Time'))

    with col2:
        calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
