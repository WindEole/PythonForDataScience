# ISINSTANCE
# Pour les NULL, le dictionnaire de l'exo précédent n'est pas approprié
# car trop de types sont problématiques : NoneType, Nan, etc...
# Pour cet exo, on utilise isinstance(object, type) : returns True if
# the specified object is of the specified type, otherwise False.


def NULL_not_found(object: any) -> int:
    """Print all types of Null."""
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and str(object) == "nan":
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool):  # bool avant int, sinon pas pris en charge
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
