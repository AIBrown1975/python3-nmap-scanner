# Cmd Line nmap scanner tool
version = "0.0.3"

# Download Dependancies automatically
if args.install:
 #   print(blue + "Installing Dependencies" + red + " root Error message can be ignored")
    pwd = os.getcwd()
    vf = open(pwd + '/dependencies.txt', 'r')
    for line in vf.readlines():
 #      cmd = ('pip3 install --user --quiet --disable-pip-version-check {} ').format(line)
        cmd = ('python3 -m pip install --user --quiet --disable-pip-version-check {} ').format(line)
        os.system(cmd)
        sys.exit()

# import modules
import os
import sys
import nmap3
import argparse
import json
from pyscanfuncts import *


blue = "\033[1;34;49m"
white = "\033[1;37;49m"
red = "\033[1;31;49m"
orange = "\033[0;31;49m"



#check user input
if not (args.host):
    print(red + "Please Spcify Host e.g (-H 127.0.0.1)" + white)
    sys.exit()

if not (args.check or args.non_check):
    print(red + "Please Enter Scan Type e.g. (--check OR --noncheck)" + white)
    sys.exit()

if not (args.tcp or args.udp or args.full):
    print(red + "Please Enter Scan Type e.g. (--t OR --u OR --A)" + white)
    sys.exit()

# Argparse if statements cycling through check and non check scans then protocols
if args.check:
    if args.tcp:
        checksynscan()
    elif args.udp:
        checkudpscan()
    elif args.full:
        checkcompscan()
elif args.non_check:
    if args.tcp:
        synscan()
    elif args.udp:
        udpscan()
    elif args.full:
        compscan()
else:
    print(help)
