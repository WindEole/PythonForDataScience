# NONLOCAL KEYWORD
# Pour rappel, les globales sont interdites. Il faut donc trouver un moyen de
# modifier des variables définies à un niveau supérieur => keyword nonlocal.


def square(x: int | float) -> int | float:
    """Return the square value of an argument."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return the exponentiation of an argument by himself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return an inner function that applies a function to x and updates x."""
    count = 0

    def inner() -> float:
        """Apply the function to the argument and modify the argument."""
        nonlocal x, count  # x aussi ! sinon, inner ne peut pas le modifier !
        count += 1
        x = function(x)
        return x

    return inner
