import PySimpleGUI as sg
from list_reservations import open_window

def main():
    layout = [[sg.Button("List reservations", key="-LIST-")],
              [sg.Button("Get reservation details", key="-DETAILS-")],
              [sg.Button("Open Window", key="-OPEN-")],
              [sg.Button("Exit", key="exit")],
              ]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "exit" or event == sg.WIN_CLOSED:
            break
        if event == "-LIST-":
            open_window()

    window.close()


if __name__ == "__main__":
    main()
