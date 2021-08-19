#!/usr/bin/python3

import nmap3
from scannerfuncts import *
import json

print("welcome to my automated nmap scanning tool")
print("created by Alex as the first module towards an automated recon tool")
print("Any problems or feedback please contact Alex in the first instance")
print("Feel free to share this with other testers")
# Scanner.py needs to be run as root, ensure sudo is used when not root



# User input to identify scan type
resp = input("""\nPlease enter the type of scan to run
                 1) Syn Scan
                 2) UDP Scan
                 3) Comprehensive Scan
                 4) Check TCP Scan
                 5) Check UDP Scan
                 6) Check Comprehensive Scan\n""")
print("you have selected option: ", resp)

#scan types called from scannerfuncts.py
if resp =='1':
    synscan()
elif resp =='2':
    udpscan()
elif resp == '3':
    compscan()
elif resp == '4':
    checksynscan()
elif resp == '5':
    checkudpscan()
elif resp == '6':
    checkcompscan()
elif resp >= '7':
    print("Please enter a valid option")




