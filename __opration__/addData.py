def add_data(data: dict, name: str, keys: list) -> dict:
    """
    this moulde get 3 argoments
    data    ->  add new user in this data
    name    ->  the name of user you wanna add it in the data
    keys    ->  information of user you wanna put it for user
    """
    if name not in data.keys():
        data[name.title()] = {key: value for key, value in zip(keys, input(
            f"Info ({", ".join(keys)}) : ").split())}
        return data
    else:
        False
