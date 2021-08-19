import nmap3
import json

print("welcome to my automated nmap scanning tool")
print("created by Alex as the first module towards an automated recon tool")
print("Any problems or feedback please contact Alex in the first instance")
print("Feel free to share this with other testers")


# User input is taken, still need to check if CIDR notation can be used
# User will be prompted to enter type of scan for inital enumeration
# Potential to add further common scan types use as smb signing etc
ip_addr = input("please enter the ip to scan:")
print("the ip you entered is: ", ip_addr)
type(ip_addr)

nmap = nmap3.Nmap()

#functions for scans
def synscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip_addr, args="-sSVC -O -vvv -oN nmap-tcp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def udpscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip_addr, args="-sU -vvv -oN nmap-udp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def compscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip_addr, args="-A -vvv -oN nmap-tcp-compscan.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def checksynscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_command(ip_addr, args="-sSVC -O -p0- -oN nmap-check-tcp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def checkudpscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_command(ip_addr, args="-sU -p0- -oN nmap-check-udp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)

def checkcompscan():
    nmap = nmap3.Nmap()
    results = nmap.scan_command(ip_addr, args="-A -p0- -oN nmap-check-comp.txt")
    print(results)
    with open('results', 'w') as outfile:
        json.dump(results, outfile)
