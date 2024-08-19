from S1E9 import Character


# __str__ VS __repr__
# Both are special methods in Python classes that are invoked to return string
# representations of objects.
# __str__: method called by the __str__() built-in function to display a
#     readable string representation of an object. It is intended to provide
#     a human-readable output. For Users ! Resumé !
# __repr__: method called by the __repr__() built-in function and by Python
#     interactive interpreter to generate a representation of the object. It
#     should be unambiguous and, ideally, should allow the object to be
#     recreated using the eval() function. For Developpers ! Detaillé !


class Baratheon(Character):
    """Representing the Baratheon Family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize attributes specific to Baratheon characters."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Change the status to dead."""
        self.is_alive = False

    def __str__(self) -> str:
        """Return a string representation of Baratheon."""
        return f"Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

    def __repr__(self) -> str:
        """Return a detailed string representation of Baratheon."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister Family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize attributes specific to Lannister characters."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """Change the status to dead."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a Lannister instance."""
        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """Return a string representation of Lannisster."""
        return f"Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

    def __repr__(self) -> str:
        """Return a detailed string representation of Lannister."""
        return self.__str__()
