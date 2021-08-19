import nmap3
import json

# User input is taken, still need to check if CIDR notation can be used
# User will be prompted to enter type of scan for inital enumeration
# Potential to add further common scan types use as smb signing etc
ip_addr = input("please enter the ip to scan:")
print("the ip you lsentered is: ", ip_addr)
type(ip_addr)

nmap = nmap3.Nmap()

#function to write output to json file for later parsing
def writefile():
    with open('', 'w') as outfile:
        json.dump(result, outfile)

#functions for scans
def synscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip_addr, args="-sSVC -O -vvv -oN nmap-tcp.txt")
    print(results)
    writefile()

def udpscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip_addr, args="-sU -vvv -oN nmap-udp.txt")
    print(results)
    writefile()

def compscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip_addr, args="-A -vvv -oN nmap-tcp-compscan.txt")
    print(results)
    writefile()

def checksynscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_command(ip_addr, args="-sSVC -O -p0- -oN nmap-check-tcp.txt")
    print(results)
    writefile()

def checkudpscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_command(ip_addr, args="-sU -p0- -oN nmap-check-udp.txt")
    print(results)
    writefile()

def checkcompscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_command(ip_addr, args="-A -p0- -oN nmap-check-comp.txt")
    print(results)
    writefile()

