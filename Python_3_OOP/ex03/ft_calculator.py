class calculator:
    """Calculator Class.

    Class that do calculation (addition, multiplication, subtraction, division)
    of vector with a scalar.
    """

    def __init__(self, values) -> None:
        """Initialise l'objet avec une liste de valeurs."""
        self.values = values

    def __str__(self) -> str:
        """Retourne une chaîne de caractères représentant l'objet."""
        return f"{self.values}"

    def __repr__(self) -> str:
        """Retourne une chaîne de caractères détaillée représentant l'objet."""
        return f"{self.values!r}"

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector and print the result."""
        if isinstance(object, (int, float)):
            self.values = [x + object for x in self.values]
            print(self)
            return self  # Return self to allow chaining if needed
        else:
            raise TypeError("Addition requires a scalar (int or float).")

    def __mul__(self, object) -> None:
        """Multiply a scalar to each element and print the result."""
        if isinstance(object, (int, float)):
            self.values = [x * object for x in self.values]
            print(self)
            return self  # Return self to allow chaining if needed
        else:
            raise TypeError("Multiplication requires a scalar (int or float).")

    def __sub__(self, object) -> None:
        """Subtract a scalar to each element and print the result."""
        if isinstance(object, (int, float)):
            self.values = [x - object for x in self.values]
            print(self)
            return self  # Return self to allow chaining if needed
        else:
            raise TypeError("Subtraction requires a scalar (int or float).")

    def __truediv__(self, object) -> None:
        """Divide each element of a vector by a scalar and print the result."""
        if isinstance(object, (int, float)):
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.values = [x / object for x in self.values]
            print(self)
            return self
        else:
            raise TypeError("Division reguires a scalar (int or float).")
