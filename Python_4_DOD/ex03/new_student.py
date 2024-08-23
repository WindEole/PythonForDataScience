import random
import string
from dataclasses import dataclass, field


# @dataclass genere automatiquement des methodes comme __init__, __repr__,
# ou __eq__ => Donc pas besoin de les définir !
# Pour les autres données à initialiser, on utilise field, on initialise à
# false pour l'init de dataclass, et redefinit dans __post_init__ !

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student."""

    name: str
    surname: str
    active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Student post initialisation (active, id, login)."""
        self.active: bool = True
        self.id: str = generate_id()
        self.login: str = self.name[0] + self.surname
