import zeep
from requests import Session
# from requests.auth import HTTPBasicAuth
# from zeep import Client, Settings, Transport
from zeep.wsse.username import UsernameToken
import os
from base64 import b64decode
import time
import subprocess

# settings = Settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)
# client = Client('http://localhost:3000/reservations/wsdl', settings=settings)
# # dd2 = client.service.get_pdf("2")
# print(client.service.get_reservation_by_code("as"))
#
# bytes = b64decode(dd2)
# print(os.getcwd())
# f = open('./my_file.pdf', 'wb')
# f.write(bytes)
# f.close()
#
# # time.sleep(3)
# path = './my_file.pdf'
# subprocess.call(["xdg-open", path])
# os.system(path)
# subprocess.Popen([path], shell=True)
#
# settings = zeep.Settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)
#
# client = zeep.Client('http://localhost:3000/reservations/wsdl', settings=settings, wsse=UsernameToken('username', 'password'))
#
# print(client.service.list())