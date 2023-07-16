import PySimpleGUI as sg
import db
from reminder import run_reminder_section

def dashboard(user):  
    sg.theme('DarkAmber')

    # Define the layout for the dashboard section
    layout_dashboard = [
        [sg.Text(f"Welcome, {user[1]}", font=("Helvetica", 25))],
        [sg.Text("Here you can view your medication schedule and access various other functions.")],
        [sg.Text("Medication Schedule", font=("Helvetica", 15))],
        [sg.Table(values=db.get_reminders(user[0]), headings=["Medication", "Interval", "Description", "Taken"], key="-REMINDER_TABLE-",
                  justification="center", auto_size_columns=False)],
        [sg.Button("Close"), sg.Button("Add Reminder")]
    ]

    # Create the dashboard window
    window_dashboard = sg.Window("MedEase - Dashboard", layout_dashboard)

    # Event loop for the dashboard window
    while True:
        event, values = window_dashboard.read()

        if event == sg.WINDOW_CLOSED or event == "Close":
            break
        if event == "Add Reminder":
            run_reminder_section(user)
            #refresh the table
            window_dashboard["-REMINDER_TABLE-"].update(values=db.get_reminders(user[0]))
        

    # Close the dashboard window
    window_dashboard.close()


