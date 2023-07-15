import PySimpleGUI as sg
from tkinter import Tk

def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    loginlayout = [  [sg.Text('Welcome to MedEase!')],
                [sg.Text('Please select your user type:')],
                [sg.Button('Patient'), sg.Button('Doctor'), sg.Button('Pharmacist'), sg.Button('Admin')],
                [sg.Button('Exit')] ]
    

    # Create the Window
    window = sg.Window('MedEase', loginlayout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        
    

    window.close()

if __name__ == '__main__':
    main()
