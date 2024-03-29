from __opration__ import readFile, addData, editData, deleteData, search, createFile
from colorama import Fore as fr


def add():
    print(fr.LIGHTWHITE_EX+f"""
{"#"*28}
    path -> url json file path for read data (example = /home/user/database/filename.json).
    name -> name of user you wanna add in this data.
    info -> you should Enter the info for any key and separate with space (example =
        keys  : [phone, job, city] ,
        value : 0912999999 programmer Tehran).
    save -> Enter path for save new data and separate with space (example =
        path = /home/user/ -> (defualt = ./)
        filename = filename.json -> (defualt = data.json)).
{"#"*28}""")
    path = input(fr.LIGHTYELLOW_EX+"Path : "+fr.LIGHTCYAN_EX)
    name = input(fr.LIGHTYELLOW_EX+"Name : "+fr.LIGHTCYAN_EX).title()
    data = readFile.readJsonFile(path)
    print()
    if data != False:
        keys = dict(list(data.values())[0]).keys()
        add_data = addData.add_data(data, name, keys)
        if add_data != False:
            save_file = input(fr.LIGHTYELLOW_EX +
                            "Save (path, filename): "+fr.LIGHTCYAN_EX).split()
            try:
                save_file[0]
                try:
                    save_file[1]
                except:
                    save_file[1] = "contant.json"
            except IndexError:
                save_file = ["./", "contant.json"]
            if createFile.create_file(data, save_file[0], save_file[1]):
                input(fr.LIGHTGREEN_EX+"[+] seccuessfly your data has been added, press Enter to return in main page..."+fr.RESET)
        else:
            input(fr.LIGHTGREEN_EX+f"[!] {fr.LIGHTYELLOW_EX+name+fr.LIGHTGREEN_EX} already exiested please try again, press Enter to return in main page...")
    else:
        input(fr.LIGHTRED_EX+f"[!] the {
              name} already existed please try again, press Enter to return in main page...")


def edit():
    print(fr.LIGHTWHITE_EX+f"""
{"#"*28}
    path -> url json file path for read data (example = /home/user/database/filename.json).
    name -> name of user you wanna edit in this data.
    wich -> select the key for edit value
    edit -> replace a new data
{"#"*28}""")
    path = input(fr.LIGHTYELLOW_EX+"Path : "+fr.LIGHTCYAN_EX)
    name = input(fr.LIGHTYELLOW_EX+"Name : "+fr.LIGHTCYAN_EX).title()
    data = readFile.readJsonFile(path)
    new_data = editData.edit_data(data, name)
    if new_data != False:
        save_file = input(fr.LIGHTYELLOW_EX +
                          "Save (path, filename) : "+fr.LIGHTCYAN_EX).split()
        try:
            save_file[0]
            try:
                save_file[1]
            except:
                save_file[1] = "contant.json"
        except IndexError:
            save_file = ["./", "contant.json"]
        if createFile.create_file(data, save_file[0], save_file[1]):
            input(fr.LIGHTGREEN_EX +
                  f"[+] seccuessfly your edit opration, press Enter to return in main page..."+fr.RESET)

        # try:
        #     if createFile.create_file(new_data, new_data[0], save_file[1]):
        #         input(
        #             fr.LIGHTGREEN_EX+f"[+] seccuessfly your edit opration, press Enter to return in main page..."+fr.RESET)
        # except IndexError:
        #     input(
        #         fr.LIGHTRED_EX+"[!] your path and filename for save have problem please try again, press Enter to return main page..."+fr.RESET)
    else:
        input(fr.LIGHTRED_EX +
              "[!] your Name not define in data please try again, press Enter to return in main page..."+fr.RESET)


def remove():
    print(fr.LIGHTWHITE_EX+f"""
{"#"*28}
    path -> path file
    name -> name of user
    save -> path for save data (path, filename) -> default(./, data.json)
{"#"*28}""")
    path = input(fr.LIGHTYELLOW_EX+"Path : "+fr.RESET)
    name = input(fr.LIGHTYELLOW_EX+"Name : "+fr.RESET).title()
    data = readFile.readJsonFile(path)
    data_removed = deleteData.delete_data(data, name)
    save_file = input(fr.LIGHTYELLOW_EX +
                      "Save (path, filename) : "+fr.LIGHTCYAN_EX).split()
    remove_access = input(fr.LIGHTYELLOW_EX+f"are you sure for remove user{fr.LIGHTGREEN_EX+name+fr.LIGHTYELLOW_EX} ({
                          fr.LIGHTRED_EX+"yes"+fr.LIGHTYELLOW_EX+", "+fr.LIGHTGREEN_EX+"no"+fr.LIGHTWHITE_EX}) : "+fr.RESET)
    if remove_access == "yes":
        try:
            save_file[0]
            try:
                save_file[1]
            except IndexError:
                save_file[1] = "contant.json"
        except IndexError:
            save_file = ["./", "contant"]
        if createFile.create_file(data_removed, save_file[0], save_file[1]):
            input(fr.LIGHTGREEN_EX+f"[+] {name} the has been removed")
        # try:
        #     if createFile.create_file(data_removed, path_save[0], path_save[1]):
        #         input(fr.LIGHTGREEN_EX+"[+] the has been removed")
        # except IndexError:
        #     input(
        #         fr.LIGHTRED_EX+"[!] your path and filename for save have problem please try again, press Enter to return main page..."+fr.RESET)
    else:
        input(fr.LIGHTWHITE_EX +
              "[!] data not removed, press Enter to return in main page..."+fr.RESET)


def _search():
    print(fr.LIGHTWHITE_EX+f"""
{"#"*28}
    path -> read data
    name -> name of user
    wich -> wich key
{"#"*28}""")
    path = input(fr.LIGHTYELLOW_EX+"Path : "+fr.RESET)
    name = input(fr.LIGHTYELLOW_EX+"Name : "+fr.RESET).title()
    data = readFile.readJsonFile(path)
    search_data = search.search_data(data, name)
    if search_data:
        input(fr.LIGHTWHITE_EX+"Press Enter to return in main page..."+fr.RESET)


def build():
    pass
