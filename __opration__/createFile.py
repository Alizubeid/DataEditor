import subprocess as sp
import json
def create_file(data: dict, file_name: str = "data.json", path: str = "./"):
    """
    this moudle get 3 argoments for build a file
    data        ->      data type should been dictionary
    file_name   ->      get file name       (defualt = data.json)
    path        ->      get path to save it (defualt = ./)
    """
    url = str(f"{path}/{file_name}")
    if sp.getoutput(f"cd {path}") == "":
        try:
            with open(url,"x") as writeFile:
                writeFile.write(json.dumps(data))
        except FileExistsError:
            get_input = input("[!] this file already exists, do you wanna replace a file (yes, no) : ")
            if get_input == "yes" or get_input == "y":
                with open(url,"w") as writeFile:
                    writeFile.write(json.dumps(data))
                return True
            else:
                return False
    else:
        return False
    

