from __get_input__ import getInput
from colorama import Fore as fr
from pyfiglet import figlet_format as banner
from os import system
from platform import uname
def cleanUp():
    os_name = uname().system
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux":
        system("clear")
    else:
        system("clear")
def print_banner():
    print(fr.LIGHTCYAN_EX+banner("Team 5")+fr.LIGHTGREEN_EX)
    print("""
team 5 telegram IDs : @amirhshf021, @Pedisdi, @Zobeid_c"""+fr.LIGHTWHITE_EX)
    text_viwe = f"""
{"#"*28}
    add            = 1
    edit           = 2
    remove         = 3
    search         = 4
    quit           = 99
    {+fr.LIGHTYELLOW_EX+}[NOTIF] -> this program just accept JSON files]{+fr.LIGHTWHITE_EX}
{"#"*28}
"""
    print(text_viwe)

def _add():
    cleanUp()
    getInput.add()

def _edit():
    cleanUp()
    getInput.edit()
def _remove():
    cleanUp()
    getInput.remove()
def _search():
    cleanUp()
    getInput._search()
def _build():
    pass

def main():
    while True:
        cleanUp()
        print_banner()
        user_input_opration=input(fr.LIGHTYELLOW_EX+"[*] wich opration you wanna used : "+fr.LIGHTCYAN_EX)
        if user_input_opration in str(list(range(1,6))+[99]):
            if user_input_opration == "1":
                _add()
            elif user_input_opration == "2":
                _edit()
            elif user_input_opration == "3":
                _remove()
            elif user_input_opration == "4":
                _search()
            elif user_input_opration == "5":
                _build()
            elif user_input_opration == "99":
                exit()
        else:
            input(fr.LIGHTRED_EX+"[!] please enter a right number, press enter to run again..."+fr.LIGHTWHITE_EX)
        



if __name__ == "__main__":
    main()
