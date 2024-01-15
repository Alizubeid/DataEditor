def delete_data(data: dict, name: str) -> dict:
    """
    this moudle get 2 argoments
    data    ->      the data you wanna remove somthing from it
    name    ->      the name you wanna remove sothing from data
    """
    return data.pop(name.title())
