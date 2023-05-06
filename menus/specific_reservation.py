import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from soap.requests import Requests
import zeep


def get_names(n):
    return f"Room number: {n.room_number}"


def open_window():
    layout = [[sg.Text('Listbox with search')],
              [sg.Column([[
                    sg.Column([
                        [sg.Text("Room number")],
                        [sg.Input('', size=(10, 20), key="-ROOM-NUMBER-", readonly=True)]
                    ]),
                  sg.Column([
                        [sg.Text("From")],
                        [sg.Input('', size=(10, 20), key="-FROM-", readonly=True)]
                    ]),
                  sg.Column([
                      [sg.Text("To")],
                      [sg.Input('', size=(10, 20), key="-TO-", readonly=True)]
                  ]),
              ]], k='layout_principal', expand_x=True)],

              [sg.Input("", key="-CODE-INPUT-")],
              [sg.Button("Check code", key='-CHECK-')],
              [sg.Button('Go back to menu', key="-EXIT-")]]
    window = sg.Window("Reservation check", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
        if event == "-CHECK-":
            print(values['-CODE-INPUT-'])
            sr = Requests()
            try:
                reservation = sr.get_reservation_by_code(values['-CODE-INPUT-'])
            except zeep.exceptions.Fault:
                sg.popup_error("No reservation with that code exists", keep_on_top=True)
                continue
            window["-ROOM-NUMBER-"].update(reservation.room_number)
            window["-FROM-"].update(reservation.from_date)
            window["-TO-"].update(reservation.to_date)
    window.close()
