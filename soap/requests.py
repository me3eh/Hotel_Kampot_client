# from zeep import Client, Settings
# import PyPDF2
#
# settings = Settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)
# client = Client('http://localhost:3000/reservations/wsdl', settings=settings)
# #dd = client.service.list()
#print(dd)
#print(type(dd))
#print(dd["_raw_elements"])
#for x in dd["_raw_elements"]:
#	print(dir(x))
#	print(x.get(0))
#pdfWriter = PyPDF2.PdfWriter()
# dd2 = client.service.get_pdf("2")
# #newFile = open(dd2, 'wb')
# #pdfWriter.write(newFile)
# #newFile.close()
# from base64 import b64decode
#
# bytes = b64decode(dd2)
# f = open('file.pdf', 'wb')
# f.write(bytes)
# f.close()
from zeep import Client, Settings
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from models.reservation import Reservation
class Requests:
    def __init__(self):
       # self.p = "hah"
       settings = Settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)
       self.client = Client('http://localhost:3000/reservations/wsdl', settings=settings)
       # dd = client.service.list()

    def getReservations(self):
        # self.p = "sadf"
        reservations_list_hash = self.client.service.list()
        reservations_list_object = []
        for res in reservations_list_hash:
            reservations_list_object.append(Reservation(res))
        return reservations_list_object
