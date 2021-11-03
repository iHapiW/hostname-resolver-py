# Avoiding Pyc Files
import sys
sys.dont_write_bytecode = True

#Importing Text Formatting Files
from pyfiglet import figlet_format
from termcolor import colored

#Importing Self-made Modules
from model.stdio import getinp
from controller import control_socket as cs

if __name__ == "__main__":
    print(colored(figlet_format("DNS Sample"),"red"))
    print(colored("\t\t---Made By iHapiW---","red"))
    DNSServer = getinp("Enter DNS Server (default 8.8.8.8): ")
    DNSServer = DNSServer if DNSServer != "" else "8.8.8.8"
    while True:
        Hostname = getinp("Enter Hostname: ")
        cs.get_ip(Hostname,DNSServer)