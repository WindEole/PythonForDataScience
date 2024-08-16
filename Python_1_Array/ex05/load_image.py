import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image.

    This function loads an image, prints its format and its pixels content
    in RGB format.

    Parameters: a string -> path to an image.jpg or image.jpeg.
    Returns: np.ndarray -> image in RGB format.
    """
    try:
        im = Image.open(path)
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
        return None
    except IOError:
        print(f"Error: Unable to open the file at path {path}.")
        return None

    # On recupère les dimensions de l'image (pillow)
    width, height = im.size

    # On détermine le mode couleur de l'image (et le nb de canaux !) (pillow)
    mode = im.mode
    if mode == "L":
        num_channels = 1  # mode niveaux de gris (1 canal)
    elif mode == "RGB":
        num_channels = 3  # mode RGB (3 canaux)
    elif mode == "RGBA":
        num_channels = 4  # mode RGBA (4 canaux)
    else:
        print(f"Error: Unsupported image mode {mode}.")
        return None

    print(f"The shape of image is: ({height}, {width}, {num_channels})")
    im.show()
    # On convertit l'image en NumPy array
    array_ori = np.array(im)
    print(array_ori)
    return array_ori
