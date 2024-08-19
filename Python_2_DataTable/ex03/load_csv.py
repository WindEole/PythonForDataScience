import pandas as pd


# FICHIER.CSV = Comma Separated Value
# C'est un fichier de base de données recueillies sans formatage,
# où chaque champ est séparé par une virgule.

def load(path: str) -> pd.DataFrame:
    """Load and returns a dataset.

    This function displays the dimensions of the data set and returns it.

    Arguments: path
    Allowed functions : pandas or any lib for data set manipulation.
    """
    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file {path} is corrupted.")
        return None
    except MemoryError:
        print(f"Error: The file {path} is too large to fit into memory.")
        return None
    except IOError:
        print(f"Error: Unable to open the file at path {path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    dataFrame = pd.DataFrame(data)
    lines, col = dataFrame.shape
    print(f"Loading dataset of dimensions ({lines}, {col})")

    # Optionnel : on vérifie si des valeurs manquent :
    # if dataFrame.isnull().values.any():
    #     print("Warning: the dataset contains missing values.")

    return dataFrame
