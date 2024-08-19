import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd


def display(data_le: pd.DataFrame, data_inc: pd.DataFrame, year: str) -> None:
    """Relation between life expectancy and income.

    This function displays the projection of life expectancy in relation
    to the gross national product for all countries in a given year.

    Arguments: Income dataFrame, Life Expectancy dataFrame, country, year.
    """
    # Reformater les données pour tf les colonnes d'années en 'year'
    data_le_melted = pd.melt(
        data_le,
        id_vars=["country"],
        var_name="year",
        value_name="life_expectancy",
        )
    data_inc_melted = pd.melt(
        data_inc,
        id_vars=["country"],
        var_name="year",
        value_name="income",
        )

    # Convertir la colonne 'year' en entier pour faciliter la fusion
    data_le_melted["year"] = data_le_melted["year"].astype(int)
    data_inc_melted["year"] = data_inc_melted["year"].astype(int)

    # Filtre les données pour l'année spécifiée
    le_filtered = data_le_melted[data_le_melted["year"] == int(year)]
    inc_filtered = data_inc_melted[data_inc_melted["year"] == int(year)]

    # Fusion des deux dataFrames sur les colonnes country et year
    merged_data = pd.merge(le_filtered, inc_filtered, on=["country", "year"])

    if merged_data.empty:
        print(f"No data available for {year}.")
        return

    # Affichage du graphique avec un référentiel
    try:
        plt.scatter(
            merged_data["income"],
            merged_data["life_expectancy"],
            color="blue",
            )
        plt.title(f"Life Expectancy vs Income in {year}")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        # Appliquer une échelle logarithmique sur l'axe X
        plt.xscale("log")

        # Formatteur personnalisé pour afficher 1k, 10k, etc.
        def log_formatter(x, pos):
            if x >= 1000:
                return f"{int(x / 1000)}k"
            else:
                return f"{int(x)}"

        plt.gca().get_xaxis().set_major_formatter(
            ticker.FuncFormatter(log_formatter)
            )
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        plt.close()
