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

layout = [[sg.Text('Listbox with search')],
          [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-')],
          [sg.Listbox(list_of_names, size=(20, 4), enable_events=True, key='-LIST-')],
          [sg.Button('Chrome'), sg.Button('Exit')]]

window = sg.Window('Listbox with Search', layout)
# Event Loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):                # always check for closed window
        break
    if values['-INPUT-'] != '':                         # if a keystroke entered in search field
        search = values['-INPUT-']
        new_values = [x for x in list_of_names if search in x]  # do the filtering
        window['-LIST-'].update(new_values)     # display in the listbox
    else:
        # display original unfiltered list
        window['-LIST-'].update(list_of_names)
    # if a list item is chosen
    # if event == '-LIST-' and len(values['-LIST-']):
    #     sg.popup('Selected ', values['-LIST-'])

window.close()