import zeep
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from models.reservation import Reservation
from base64 import b64decode
import subprocess
from zeep.wsse.username import UsernameToken

class Requests:
    def __init__(self):
        settings = zeep.Settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)

        self.client = zeep.Client('http://localhost:3001/reservations/wsdl', settings=settings,
                                  wsse=UsernameToken('username', 'password'))

    def get_reservations(self):
        reservations_list_hash = self.client.service.list()
        reservations_list_object = []
        for res in reservations_list_hash:
            reservations_list_object.append(Reservation(res))
        return reservations_list_object

    def get_pdf_confirmation(self, number):
        result = self.client.service.get_pdf(f"{number}")
        bytes = b64decode(result["pdf"])
        filename = result['pdf_name']
        filepath = f"./{filename}"

        f = open(filepath, 'wb')
        f.write(bytes)
        f.close()

        subprocess.call(["xdg-open", filepath])

    def get_reservation_by_code(self, number):
        return Reservation(self.client.service.get_reservation_by_code(f"{number}"))
