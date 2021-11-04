from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
init()

#Initializing Custom Input Output Function For More Coloful + Readable UI

def success(title,text : str):
    print(colored(figlet_format("[  "+title+"  ]"),"green"))
    for line in text.split("\n"):
        print(colored("[+]\t"+line,"green"))

def error(text : str):
    print(colored(figlet_format("["+text+"]"),"red"))
