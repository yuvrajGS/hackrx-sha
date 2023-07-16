import PySimpleGUI as sg
import time
import simpleaudio as sa
from db import store_reminder

def play_reminder_sound():
    wave_obj = sa.WaveObject.from_wave_file("reminder_sound.wav") 
    play_obj = wave_obj.play()
    play_obj.wait_done()

def run_reminder_section(user):
    # Define the layout for the reminder section
    layout_reminder = [
        [sg.Text("Medication Name"), sg.Input(key="-MEDICATION-NAME-")],
        [sg.Text("Interval (in hours)"), sg.Input(key="-INTERVAL-", enable_events=True)],
        [sg.Text("Description/Note"), sg.Input(key="-DESCRIPTION-")],
        [sg.Button("Add Reminder"), sg.Button("Close")]
    ]

    # Create the reminder window 
    window_reminder = sg.Window("MedEase - Reminder", layout_reminder, finalize=True)

    # Event loop for the reminder window
    flag=False
    interval=0
    while True:
        event, values = window_reminder.read()

        if event == sg.WINDOW_CLOSED or event == "Close":
            break
        if event == "Take Medication":
            play_reminder_sound()

        if event == "Add Reminder":
            flag = True
            medication_name = values["-MEDICATION-NAME-"]
            interval = int(values["-INTERVAL-"])
            description = values["-DESCRIPTION-"]

            # Store the reminder in the database
            store_reminder(user[0], medication_name, interval, description)
            #exit back to dashboard
            break

    # Close the reminder window
    window_reminder.close()

    # Check reminder time and play sound
    if flag:
        reminder_time = time.strftime("%H:%M:%S", time.localtime(time.time() + interval))
        while True:
            current_time = time.strftime("%H:%M:%S")

            if current_time == reminder_time:
                play_reminder_sound()
                break

        
