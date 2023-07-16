import PySimpleGUI as sg

def dashboard():
    # Define the layout for the dashboard section
    layout = [
        [sg.Text("Dashboard", font=("Helvetica", 25))],
        [sg.Text("Welcome to the dashboard! Here you can view your medication schedule and access various other functions.")],
        [sg.Text("Medication Schedule", font=("Helvetica", 15))],
    ]

    # Create the dashboard window 
    window_reminder = sg.Window("Medication Maven - Dashboard", layout, finalize=True)


    # Event loop for the dashboard window
    while True:
        event, values = window_reminder.read()

        if event == sg.WINDOW_CLOSED or event == "Close":
            break

    # Close the reminder window
    window_reminder.close()

