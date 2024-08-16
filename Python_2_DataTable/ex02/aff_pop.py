import matplotlib.pyplot as plt
import pandas as pd


def display(data: pd.DataFrame, country1: str, country2: str) -> None:
    """Display the data for two given countries on the same graph."""
    if country1 not in data["country"].values:
        print(f"Error: The country {country1} is not in the dataset.")
        return
    if country2 not in data["country"].values:
        print(f"Error: The country {country2} is not in the dataset.")
        return

    # Filtre les donnés pour le pays spécifié
    country1_data = data[data["country"] == country1].drop(columns=["country"])
    country2_data = data[data["country"] == country2].drop(columns=["country"])

    # Transposer les données pour avoir les années en index
    country1_data = country1_data.T
    country1_data.columns = [country1]  # On renomme la colonne
    country1_data.index = pd.to_datetime(country1_data.index, format="%Y")

    country2_data = country2_data.T
    country2_data.columns = [country2]  # On renomme la colonne
    country2_data.index = pd.to_datetime(country2_data.index, format="%Y")

    # Conversion des valeurs formatées avec "M" ou "k" en valeurs numériques
    country1_data[country1] = pd.to_numeric(country1_data[country1].replace(
        {"M": "e6", "k": "e3"}, regex=True)
        )
    country2_data[country2] = pd.to_numeric(country2_data[country2].replace(
        {"M": "e6", "k": "e3"}, regex=True)
        )

    # Fusionner les deux DataFrames sur les années
    combined_data = pd.concat([country1_data, country2_data], axis=1)

    # Affichage du graphique avec un référentiel
    try:
        plt.plot(
            combined_data.index,
            combined_data[country1],
            linestyle="-",
            color="green",
            label=country1,
        )
        plt.plot(
            combined_data.index,
            combined_data[country2],
            linestyle="-",
            color="blue",
            label=country2,
        )
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")  # Ajoute une légende

        # Ajuster la graduation de l'axe y pour afficher des valeurs en million
        plt.gca().get_yaxis().set_major_formatter(
            plt.FuncFormatter(lambda x, _: f"{x * 1e-6:.1f}M")
        )

        # Limiter l'affichage de l'axe x
        plt.xlim(pd.to_datetime("1800"), pd.to_datetime("2050"))
        plt.xticks(rotation=45)  # Rotation du label de l'axe X (lisibilité)
        plt.tight_layout()  # Ajuste la mise en page pour éviter chevauchement
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        plt.close()  # ferme proprement la fenetre de display
