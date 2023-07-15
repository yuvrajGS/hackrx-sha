import PySimpleGUI as sg
import MedEase
From tkinter import Tk

def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Welcome to MedEase!')],
                [sg.Text('Please select your user type:')],
                [sg.Button('Patient'), sg.Button('Doctor'), sg.Button('Pharmacist'), sg.Button('Admin')],
                [sg.Button('Exit')] ]
    

    # Create the Window
    window = sg.Window('MedEase', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        elif event == 'Patient':
            window.close()
            MedEase.patient()

        #patient
            def formatLR(Meditation):
        return [
            sg.Listbox(['Add Medication'],size=(60,6),key=f'input-{Medication}', select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, pad=(0,5))
        ]
    layoutR = [
        [sg.Text('Yuvraj Opt-out:')], formatLR('Yuvraj'), 
        [sg.Text('Meer Opt-out:')], formatLR("Meer"), 
        [sg.Text('Thenu Opt-out:')], formatLR("Thenu"), 
        [sg.Text('Cynthia Opt-out:')], formatLR("Cynthia"), 
        [sg.Text('Sarah Opt-out:')], formatLR("Sarah")

    
        elif event == 'Doctor':
            window.close()
            MedEase.doctor()
        elif event == 'Pharmacist':
            window.close()
            MedEase.pharmacist()
        elif event == 'Admin':
            window.close()
            MedEase.admin()
    window.close()