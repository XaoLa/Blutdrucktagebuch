import streamlit as st
from streamlit_calendar import calendar
import pandas as pd
from functions.login import *
from functions.dataHandler import DataHandler
from datetime import datetime, timedelta

calendar_options = {
    "editable": "false",
    "selectable": "false",
    "timeZone": 'UTC',
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "00:00:00",
    "slotMaxTime": "24:00:00",
    "initialView": "resourceTimelineDay",
    # "resourceGroupField": "Werte",
    "resources": [
        {"id": "a", "field": "Systol", "title": "Systol"},
        {"id": "b", "field": "Dystol", "title": "Dystol"},
    ],
}

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
default_item_A = {"title": "0", "start": "0000-00-00T00:00:00", "end": "0000-00-00T00:00:00", "resourceId": "a"}
default_item_B = {"title": "0", "start": "0000-00-00T00:00:00", "end": "0000-00-00T00:00:00", "resourceId": "b"}


st.set_page_config(page_title="Hauptseite", page_icon="📈", layout="wide")

@st.experimental_dialog("Daten eingeben")
def edit(item):
    entryData = searchForItem(item["title"], item["start"][:-1], item["end"][:-1])
    value = st.text_input("Wert", item["title"])
    if st.button("Submit"):
        entryData["title"] = value
        handler.save_object(fileName="EventTable.csv", obj=st.session_state.calendarEvents, commit_message="Updaten")
        st.rerun()

    if st.button("Löschen"):
        handler.delete_object(commit_message="Loeschen")
        st.rerun()


@st.experimental_dialog("Daten eingeben")
def create(item):
    value = st.text_input("Wert")
    if st.button("Submit"):
        resourceId = item["resource"]["id"]
        # to remove last part of unwanted date
        trimmedDate = item["date"][:-5]
        newData = {"title": value, "start": trimmedDate, "end": addHalfHour(trimmedDate), "resourceId": resourceId}
        st.session_state.calendarEvents.append(newData)
        handler.save_object(fileName="EventTable.csv", obj=st.session_state.calendarEvents, commit_message="Erstellen")
        st.rerun()

def searchForItem(target_title, target_start, target_end):
    return next((d for d in st.session_state.calendarEvents if d["title"] == target_title and d["start"] == target_start and d["end"] == target_end), None)

def addHalfHour(dateString):
    # Convert the UTC string to a datetime object
    original_datetime = datetime.strptime(dateString, "%Y-%m-%dT%H:%M:%S")
    future_datetime = original_datetime + timedelta(minutes=30)
    # Convert the modified datetime object back to a string
    return future_datetime.strftime("%Y-%m-%dT%H:%M:%S")

def filterFunctionA(x):
    return x["resourceId"] == "a"

def filterFunctionB(x):
    return x["resourceId"] == "b"

def fill_missing_slots(data, time_range, default_item):
    filled_data = []
    data_dict = {item["start"]: item for item in data}
    for time in time_range:
        time_str = time.strftime('%Y-%m-%dT%H:%M:%S')
        if time_str in data_dict:
            filled_data.append(data_dict[time_str])
        else:
            default_item_copy = default_item.copy()
            default_item_copy["start"] = time_str
            filled_data.append(default_item_copy)
    return filled_data

main()  # sets the authentication status
# Handle authentication status
if st.session_state["authentication"]:
    handler = DataHandler(githubContents=st.session_state.github)
    st.session_state.calendarEvents = handler.load_object("EventTable.csv") or []
    sortedList = sorted(st.session_state.calendarEvents, key=lambda x: x["start"])
    filteredSystolData = list(filter(filterFunctionA, sortedList))
    filteredDystolData = list(filter(filterFunctionB, sortedList))

    # Fill missing slots for both lists
    time_range = pd.date_range(start='2024-06-03T00:00:00', end='2024-06-03T23:59:00', freq='30T')
    systolData = fill_missing_slots(filteredSystolData, time_range, default_item_A)
    dystolData = fill_missing_slots(filteredDystolData, time_range, default_item_B)
    data = {
        "Systol": [float(item["title"]) for item in systolData],
        "Dystol": [float(item["title"]) for item in dystolData],
        "Time": time_range
    }
    df = pd.DataFrame(data)
    df.set_index('Time', inplace=True)

    st.title('Übersicht')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.line_chart(df)

    with col2:
        calendar = calendar(events=st.session_state.calendarEvents, options=calendar_options, custom_css=custom_css)

    if calendar.get("eventClick"):
        edit(calendar["eventClick"]["event"])
    if calendar.get("dateClick"):
        create(calendar["dateClick"])

    st.write(f'Welcome *{st.session_state["username"]}*')
    logout_button = st.button("Logout")
    if logout_button:
            st.session_state['authentication'] = False
            st.rerun()
