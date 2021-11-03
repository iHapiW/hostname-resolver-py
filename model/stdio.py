import sys

from readchar import readchar
from termcolor import colored
from colorama import init
init()

#Initializing Custom Input Output Function For More Coloful + Readable UI

def getinp(text : str):
    sys.stdout.write(colored("\n[*] "+text,"blue"))
    return sys.stdin.readline()[:-1]

def success(text : str):
    sys.stdout.write(colored("\n[+] "+text+"\n","green"))

def warning(text : str):
    sys.stdout.write(colored("\n[!] "+text+"\n","yellow"))

def error(text : str):
    sys.stdout.write(colored("\n[-] "+text,"red"))
    readchar()
    print("")
    sys.exit()
