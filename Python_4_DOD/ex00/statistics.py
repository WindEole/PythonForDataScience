from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Perfoms statistic operations on an unknown quantity of arguments."""

    # 1) On regarde si on a des valeurs numériques et on les convertit en liste
    values = sorted([arg for arg in args if isinstance(arg, (int, float))])
    if not values:
        print("ERROR")
        return

    # 2) Calcul de la moyenne (mean)
    mean = sum(values) / len(values)

    # 3) Calcul de la mediane (median)
    n = len(values)
    if n % 2 == 1:
        median = values[n // 2]
    else:
        median = (values[n // 2 - 1] + values[n // 2]) / 2

    # 4) Calcul des percentile 25% et 75% (quartile 50% = mediane) (quartile)
    def percentile(data, percentile):
        """Calculate the quartiles of a list of values."""
        index = (len(data) - 1) * percentile / 100.0
        lower = int(index)
        upper = lower + 1
        if upper >= len(data):
            return data[lower]
        return data[lower] + (data[upper] - data[lower]) * (index - lower)

    q25 = percentile(values, 25)
    q75 = percentile(values, 75)

    # 5) Calcul de la variance (variance)
    variance = sum((x - mean) ** 2 for x in values) / len(values)

    # 6) Calcul de l'écart-type (standard deviation)
    std_dev = variance ** 0.5

    # print(kwargs)
    # 7) On récupère les kwargs
    authorized = ['mean', 'median', 'quartile', 'std', 'var']
    for key, stat in kwargs.items():  # Parcours des paires clé-valeur
        if stat not in authorized:
            print("ERROR")
            continue
        # 8) Affichage des statistiques en fonction de kwargs
        if stat == "mean":
            print(f"mean : {mean}")
        elif stat == "median":
            print(f"median : {median}")
        elif stat == "quartile":
            print(f"quartile : [{q25}, {q75}]")
        elif stat == "std":
            print(f"std : {std_dev}")
        elif stat == "var":
            print(f"var : {variance}")
        else:
            print("ERROR")
