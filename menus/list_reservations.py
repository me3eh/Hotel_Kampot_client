import PySimpleGUI as sg
import sys
import os
from soap.requests import Requests
import zeep

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from models.quit_exception import QuitException


def get_names(n):
    return f"Room number: {n.room_number}"


def fill_listbox_with_reservations(window):
    sr = Requests()

    try:
        reservation_list = sr.get_reservations()
    except zeep.exceptions.Fault:
        sg.popup_error("There are no reservations left")
        raise QuitException("haha")

    reservation_list_names = list(map(get_names, reservation_list))
    window["-LIST-"].update(reservation_list_names)
    return reservation_list

def open_window():
    try:
        layout = [[sg.Text('Listbox with search')],
                  [sg.Column([[
                        sg.Listbox([], size=(20, 4), enable_events=True, key='-LIST-'),
                        sg.Column([
                            [sg.Text("Room number")],
                            [sg.Input('Multiline\n', size=(10, 20), key="-ROOM-NUMBER-", readonly=True)]
                        ]),
                      sg.Column([
                            [sg.Text("From")],
                            [sg.Input('Multiline\n', size=(10, 20), key="-FROM-", readonly=True)]
                        ]),
                      sg.Column([
                          [sg.Text("To")],
                          [sg.Input('Multiline\n', size=(10, 20), key="-TO-", readonly=True)]
                      ]),
                  ]], k='layout_principal', expand_x=True)],

                  [sg.Button("Buy", key='-BUY-')],
                  [sg.Button('Go back to menu', key="-EXIT-")]]
        window = sg.Window("Reservation list", layout, modal=True, finalize=True)
        reservation_list = fill_listbox_with_reservations(window=window)
        if reservation_list is False:
            return

        while True:
            event, values = window.read()

            if event == "-EXIT-" or event == sg.WIN_CLOSED:
                break
            if event == "-LIST-":
                print(event)
                print(values)
                index = window["-LIST-"].get_indexes()[0]
                reservation = reservation_list[index]
                window["-ROOM-NUMBER-"].update(reservation.room_number)
                window["-FROM-"].update(reservation.from_date)
                window["-TO-"].update(reservation.to_date)
            if event == "-BUY-":
                index = window["-LIST-"].get_indexes()
                if len(index) == 0:
                    sg.popup_error('Firstly select some reservation')
                    continue
                val = sg.popup_ok_cancel('Are you sure you want to buy reservation for this room?', keep_on_top=True)
                index = window["-LIST-"].get_indexes()
                print(index)
                if val == "OK":
                    sg.popup('You bought reservation. Click ok to show pdf confirmation')
                    sr = Requests()
                    sr.get_pdf_confirmation(reservation_list[index[0]].id)
                    reservation_list = fill_listbox_with_reservations(window=window)
                    if reservation_list is False:
                        window.close()
        window.close()
    except QuitException:
        window.close()
