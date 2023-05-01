import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
# print(os.getcwd())
from soap.requests import Requests
from models.reservation import Reservation

def get_names(n):
    return n.getRoomNumber()

sr = Requests()
reservation_list = sr.getReservations()
reservation_list_names = list(map(get_names, reservation_list))


def open_window():
    layout = [[sg.Text('Listbox with search')],
              [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-')],
              [sg.Listbox(reservation_list_names, size=(20, 4), enable_events=True, key='-LIST-')],
              [sg.Button("Buy", size=(20, 4), key='-LIST-')],
              [sg.Button('Chrome'), sg.Button('Exit')]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()