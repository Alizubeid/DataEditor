import json


def readJsonFile(path: str ) -> dict:
    """
    this moudle get 1 argoment
    path    ->      the json path your database save it there (example = /home/username/database/names.json)
    """
    try:
        with open(path) as myFile:
            return json.loads(myFile.read())
    except FileNotFoundError:
        return False
