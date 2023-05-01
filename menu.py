import PySimpleGUI as sg
from soap import SoapRequests
from models.reservation import Reservation

sr = SoapRequests()
reservation_object_list = []
list_of_names = []

def initialize():
    reservations_list = sr.get_reservations()
    for reservation in reservations_list:
        reservation_object_list.append(Reservation(reservation))
    list_of_names = list(map(get_names, reservation_object_list))
    # print(list_of_names)
    return list_of_names

def get_names(n):
    return n.getRoomNumber()
# names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
#          'Andrea', 'Meredith', 'Deborah', 'Pauline',
#          'Belinda', 'Wendy']
list_of_names = initialize()
print(list_of_names)
print(str(reservation_object_list))

def open_window():
    layout = [[sg.Text('Listbox with search')],
              [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-')],
              [sg.Listbox(list_of_names, size=(20, 4), enable_events=True, key='-LIST-')],
              [sg.Button('Chrome'), sg.Button('Exit')]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    layout = [[sg.Button("Open Window", key="open")]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            open_window()

    window.close()


if __name__ == "__main__":
    main()