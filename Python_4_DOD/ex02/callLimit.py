from typing import Any

# WRAPPER
# Cet exercice vise à définir un wrapper (ou décorateur). Un Decorateur prend
# une fonction en entrée et retourne une nouvelle fonction qui ajoute des
# fonctionnalités à la fonction initiale.

# callable : Annotation de type qui spécifie que la fonction retourne un objet
# que l'on peut appeler comme une fonction.

# hex(id(function)) : id(function) -> accès à l'adresse mémoire de la fonction
# hex(...) -> convertit l'identifiant en hexadecimal


def callLimit(limit: int) -> callable:  # Càd qu'elle retourne un decorateur !
    """Block the execution of a function after a given limit."""
    count = 0

    def callLimiter(function: callable) -> callable:  # capture la fct cible !
        """Capture a given function and closure."""

        def limit_function(*args: Any, **kwds: Any) -> None:
            """Count the number of executions."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(
                    f"Error: <function '{function.__name__}' "
                    f"at {hex(id(function))}> call too many times"
                    )
        return limit_function
    return callLimiter
