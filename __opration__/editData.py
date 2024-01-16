from colorama import Fore as fr
def edit_data(data: dict, name: str) -> dict:
    """
    this moudle get 4 argoments
    data        ->  the data you wanna edit somthig from it
    name        ->  name of user you
    keyName     ->  key of user info (example = phone, age)
    user_input  ->  insert new data into keyName from user
    """
    if name in list(data.keys()):
        keys = data[name].keys()
        key = input(fr.LIGHTYELLOW_EX+f"Wich ({", ".join(keys)}) : "+fr.RESET)
        if key not in keys:
            input(fr.LIGHTRED_EX+"[!] your key not define in data please try again, press Enter to return in main page..."+fr.RESET)
            return False
        info = input(fr.LIGHTYELLOW_EX+f"Edit ({key} = {data[name][key]}) : "+fr.RESET)
        data[name][key] = info
    else:
        return False
    return data

