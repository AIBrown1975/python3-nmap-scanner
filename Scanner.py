#!/usr/bin/python3

# Scanner.py needs to be run as root, ensure sudo is used when not root

import nmap3
from scannerfuncts import *


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




