import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ft_rotate(path: str) -> np.ndarray:
    """Rotate an image.

    This function loads an image, converts it to grayscale (1 channel), slices
    it to a new width and height, rotates it and displays it using Matplotlib.

    Parameters: a string -> path to an image.jpg or image.jpeg.
    Returns: np.ndarray -> image in grayscale format.
    """
    try:
        im = Image.open(path)
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
        return None
    except IOError:
        print(f"Error: Unable to open the file at path {path}.")
        return None

    # On convertit l'image en NumPy array
    im_array = np.array(im)

    # Vérifier que l'image est bien en RGB
    if im_array.ndim != 3 or im_array.shape[2] != 3:
        raise ValueError("The image is not in RGB format.")

    # On "zoome" sur l'image (en réalité on slice l'array 2D)
    im_array_sliced = im_array[100:500, 450:850]

    # On convertit l'array sliced en Image
    zoom_ori = Image.fromarray(im_array_sliced)

    # On convertit l'image en niveaux de gris (1 canal)
    zoom_gray = zoom_ori.convert("L")
    zoom = zoom_gray.transpose(method=Image.Transpose.ROTATE_90)
    # On récupère les attributs de l'image zoomée
    width, height = zoom.size
    mode = zoom.mode
    if mode == "L":
        num_channels = 1  # mode niveaux de gris (1 canal)
    elif mode == "RGB":
        num_channels = 3  # mode RGB (3 canaux)
    elif mode == "RGBA":
        num_channels = 4  # mode RGBA (4 canaux)
    else:
        print(f"Error: Unsupported image mode {mode}.")
        return None

    print(f"The shape of image is: ({height}, {width}, {num_channels}) or ({height}, {width}))")
    # On recupère le canal RED, mais on ajoute une dimension au tableau (0:1)
    im_array_red = im_array_sliced[:, :, 0:1]
    print(im_array_red)
    print(f"New shape after Transpose: ({height}, {width})")
    im_array_final = im_array_sliced[:, :, 0]
    print(im_array_final)

    # Affichage de l'image avec un référentiel GRAYSCALE
    try:
        plt.imshow(zoom, cmap="gray")
        plt.title("Zoomed Image (Grayscale)")
        plt.xlabel("x (width)")
        plt.ylabel("y (height)")
        # Inverser l'axe Y pour correspondre à la convention d'affichage des images
        # plt.gca().invert_yaxis() => pas besoin !
        # Afficher une grille
        # plt.grid(True)
        # Display l'image avec le référentiel
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        plt.close() # ferme proprement la fenetre de display

    return (im_array_sliced)
