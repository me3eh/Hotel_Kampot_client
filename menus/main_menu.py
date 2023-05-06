import PySimpleGUI as sg
from list_reservations import open_window
from models.quit_exception import QuitException
from specific_reservation import open_window as open_window_reservation

def main():
    layout = [[sg.Button("List reservations", key="-LIST-")],
              [sg.Button("Get reservation details", key="-DETAILS-")],
              [sg.Button("Exit", key="-EXIT-")],
              ]
    window = sg.Window("Hotel Kampot - Reservations", layout)
    while True:
        event, values = window.read()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
        elif event == "-LIST-":
            try:
                open_window()
            except QuitException:
                pass

        elif event == "-DETAILS-":
            open_window_reservation()

    window.close()


if __name__ == "__main__":
    main()
