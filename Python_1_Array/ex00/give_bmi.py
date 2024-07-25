import sys

# BMI = Body Mass Index (Indice de Masse Corporelle)
# grandeur qui estime la corpulence d'une personne, se calcule en fonction de
# la taille et du poids : BMI = masse en kg / (taille en m au carré)

# methode ZIP()
# zip prends des iterables, les agrege en tuple et les retourne.
# https://www.programiz.com/python-programming/methods/built-in/zip

# difference assert / raise pour gestion d'erreurs :
# assert -> verifications internes pdt le dvlpmt. Les asserts peuvent être
#   désactivés lors de l'exécution avec l'option d'optimisation -o.
# raise -> lève des exceptions officielles (ValueError / TypeError...) lors
# d'erreurs d'entrées de fonction. Non désactivables !


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Compute the Body Mass Index for each pair of height and weight.

    Paramètres:
    height (list of int/float): list of heights in meters.
    weight (list of int/float): list of weights in kilograms.

    Returns: list of int/float of BMI values.
    """
    # Vérifier que les listes ont la même longueur
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of same length.")
    # Vérifier que les listes ne contiennent que int ou float
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Height list contains non-numeric elements.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Weight list contains non-numeric elements.")

    # calculer le BMI pour chaque paire de valeurs height/weight
    zipped = zip(height, weight)
    bmi = [w / (h**2) for h, w in zipped]
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values.

    Paramètres:
    bmi (list of int/float): list of BMI values.
    limit (int): the limit to apply.

    Returns: list of booleans indicating it the BMI is below the limit.
    """
    # Vérifier que la liste ne contient que int ou float
    if not all(isinstance(item, (int, float)) for item in bmi):
        raise TypeError("BMI list contains non-numeric elements.")
    # Vérifier que limit est un int
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    return [item < limit for item in bmi]


def main(arg1, arg2):
    list1 = [float(item) for item in arg1.split(",")]

    try:
        if arg2.isdigit():
            limit = int(arg2)
            weight = []  # pas de poids si arg2 est un seuil
        else:
            weight = [float(item) for item in arg2.split(",")]
            limit = float("inf")  # pas de seuil si on a des poids

        if limit == float("inf"):
            bmi = give_bmi(list1, weight)
            print(f"{bmi}, {type(bmi)}")

        if limit != float("inf"):
            limit_applied = apply_limit(list1, limit)
            print(f"{limit_applied}")
    except (ValueError, TypeError) as msg:
        print(msg)


if __name__ == "__main__":
    try:
        assert (len(sys.argv) == 3), (
            "AssertionError: Incorrect number of arguments."
        )
        main(sys.argv[1], sys.argv[2])
    except AssertionError as msg:
        print(msg)
