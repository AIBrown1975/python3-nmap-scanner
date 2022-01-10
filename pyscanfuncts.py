import os
import nmap3
import argparse
import json
import textwrap

blue = "\033[1;34;49m"
white = "\033[1;37;49m"
red = "\033[1;31;49m"
orange = "\033[1;31;43m"

# Argparse arguments
parser = argparse.ArgumentParser(
    prog='Pyscan Version 0.0.3',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''\
        Additional Information:
            Automated Nmap Scanner written using Python3-Nmap
            Created by Alex Brown in conjunction with Craig Dowey and Tom McDowell
            for use on both CHECK and Non-CHECK penetration tests
            Any issues should be reported to Alex in the first instance
        '''))
parser.add_argument("-H", "--host", type=str, help="hosts to scan")
parser.add_argument("-i","--install",action="store_true",dest="install",help="install dependencies")
parser.add_argument("--check", action="store_true", help="set scan type to be CHECK")
parser.add_argument("--non-check", action="store_true", help="set scan to non CHECK, will scan top 100 ports")
group = parser.add_mutually_exclusive_group()
group.add_argument("-t", "--tcp", action="store_true", help="set scan protocol to tcp")
group.add_argument("-u", "--udp", action="store_true", help="set scan protocol to udp")
group.add_argument("-A", "--full", action="store_true", help="set scan to comprehensive scan")
args = parser.parse_args()

# Scan types to be called 
def synscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(args.host, args="-sSVC -O -vvv -oN nmap-tcp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def udpscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(args.host, args="-sU -vvv --min-rate=5000 -oN nmap-udp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def compscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(args.host, args="-A -vvv -oN nmap-tcp-compscan.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def checksynscan():
    nmap = nmap3.Nmap()
    print(orange + "Full Port Script Scan - May take a while!" + white)
    results = nmap.scan_command(args.host ,arg="-p0-", args="-sSVC -O -oN nmap-check-tcp.txt")
    cmd = ('cat nmap-check-tcp.txt')
    os.system(cmd)

def checkudpscan():
    nmap = nmap3.Nmap()
    print(orange + "Full Port UDP Scan - May take a while!" + white)
    results = nmap.scan_command(args.host ,arg="-p0-", args="-sU --min-rate=5000 -oN nmap-check-udp.txt")
    cmd = ('cat nmap-check-udp.txt')
    os.system(cmd)

def checkcompscan():
    nmap = nmap3.Nmap()
    print(orange + "Full Port Comprehensive Scan - May take a while!" + white)
    results = nmap.scan_command(args.host ,arg="-p0-", args="-A -oN nmap-check-comp-tcp.txt")
    cmd = ('cat nmap-check-comp-tcp.txt')
    os.system(cmd)