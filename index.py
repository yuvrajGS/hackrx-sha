import PySimpleGUI as sg
import db
from main import dashboard
#login flag
flag = False
# Connect to the MySQL database
cursor = db.cursor
#theme
sg.theme('DarkAmber')
# Define the layout for the login screen
layout_login = [
    [sg.Image("logo.png",expand_x=True,expand_y=True)],
    [sg.Text("Username: "), sg.Input(key="-USERNAME-")],
    [sg.Text("Password: "), sg.Input(key="-PASSWORD-", password_char="*")],
    [sg.Button("Login")]
]

# Create the login window
window_login = sg.Window("MedEase - Login", layout_login)

# Event loop for the login window

while True:
    event, values = window_login.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Login":
        username = values["-USERNAME-"]
        password = values["-PASSWORD-"]

        # Verify the login credentials
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            # Close the login window and open the main window
            flag = True
            window_login.close()
            dashboard(user)
            break
        else:
            sg.popup("Invalid username or password")

# Close the login window
window_login.close()
