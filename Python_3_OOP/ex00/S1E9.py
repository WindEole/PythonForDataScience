from abc import ABC, abstractmethod


# ABC = Abstract Base Classes -> classe abstraite !
class Character(ABC):
    """Character Class."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize attributes first_name and is_alive."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Abstract method that set the death of the character."""
        pass

    def __str__(self) -> str:
        """Return a string representation of the character."""
        return f"{self.first_name}, {'Alive' if self.is_alive else 'Dead'}"

    # !r dans une f-string : invoque la fonction repr() sur l'expression ou la
    # variable correspondante. Il convertit la valeur de l'expression en une
    # forme plus détaillée et non ambiguë, utile ensuite pour recréer l'objet.
    # !r appelle repr()
    # !s appelle str() -> option par défaut donc pas besoin de préciser
    # !a appelle ascii() pour échapper les caractères non-ASCII
    def __repr__(self) -> str:
        """Return a detailed string representation of the character."""
        return (
            f"Character(first_name={self.first_name!r}, "
            f"is_alive={self.is_alive})"  # !r inutile car booleen ! str=repr
        )


# On a une classe abstraite, maintenant : classe concrète !
class Stark(Character):
    """Representing the Stark Family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize attributes specific to Stark characters."""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Change the status to dead."""
        self.is_alive = False
