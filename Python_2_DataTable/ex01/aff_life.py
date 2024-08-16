import matplotlib.pyplot as plt
import pandas as pd


def display(data: pd.DataFrame, country: str) -> None:
    """Display the data for a given country."""
    if country not in data["country"].values:
        print(f"Error: The country {country} is not in the dataset.")
        return

    # Filtre les donnés pour le pays spécifié
    country_data = data[data["country"] == country].drop(columns=["country"])
    # Ce qu'on obtient après filtrage, c'est un tableau avec les années en
    # colonne et les esperances de vie en lignes :
    # 1800   1801   1802 ...
    # 27.2   27.3   27.4 ...
    # Pour l'affichage graphique, on a besoin d'inverser lignes et colonnes
    # on va donc utiliser la méthode T (Transpose) de l'objet DataFrame

    # Transposer les données pour avoir les années en index
    country_data = country_data.T
    country_data.columns = [country]  # On renomme la colonne
    country_data.index = pd.to_datetime(country_data.index, format="%Y")
    # on transforme les int représentant des annees en objets datetime
    # pour bénéficier de fonctionnalités de traitement des dates de Matplotlib

    # Affichage du graphique avec un référentiel
    try:
        # plt.figure(figsize=(12, 6))
        # plt.plot(
        #     country_data.index,
        #     country_data[country],
        #     marker="o",
        #     markersize=1,
        #     linestyle="-"
        # )
        plt.plot(country_data.index, country_data[country], linestyle="-")
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        # plt.grid(True)
        plt.xticks(rotation=45)  # Rotation du label de l'axe X (lisibilité)
        plt.tight_layout()  # Ajuste la mise en page pour éviter chevauchement
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        plt.close()  # ferme proprement la fenetre de display
