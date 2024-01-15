from colorama import Fore as fr
def search_data(data: dict,name : str) -> str:
    """
    this moudle get 3 argoments
    data    ->      the data you wanna find something from it
    name    ->      name of user you wanna find info from data
    key     ->      key name of info you wanna find from data
    """
    if name in list(data.keys()):
        keys = list(list(data.values())[0].keys())
        key = input(fr.LIGHTYELLOW_EX+f"Wich ({", ".join(keys)}) : "+fr.RESET)
        if key in keys:
            print(fr.LIGHTYELLOW_EX+f"{key} {fr.LIGHTWHITE_EX+":"+fr.LIGHTGREEN_EX} {data[name][key]}"+fr.RESET)
            return True
        else:
            input(fr.LIGHTRED_EX+"[!] your key not define please try again, Press Enter to return in main page..."+fr.RESET)
            return False
    else:
        input(fr.LIGHTRED_EX+f"[!] name of user {fr.LIGHTWHITE_EX+name+fr.LIGHTRED_EX} not define please try again, Press Enter to return in main page..."+fr.RESET)
        return False