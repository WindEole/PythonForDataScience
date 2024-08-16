import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_show_image(array, title):
    """Display Image."""
    res_im = Image.fromarray(array)
    try:
        plt.imshow(res_im)
        plt.title(title)
        plt.axis("off")  # Display l'image sans le référentiel
        plt.show()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        plt.close()  # ferme proprement la fenetre de display


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    # Consigne : on peut utiliser les operateurs =, +, -, *
    # result = np.invert(array) NON ! Le sujet demande en fait une OPERATION
    #  VECTORISEE : 255 - array, cad appliquée à chaque élément de l'array
    # sans nécessiter de boucles explicites.
    # Pour inverser des couleurs, on soustrait chaque valeur au max 255
    invert_array = 255 - array
    ft_show_image(invert_array, "Invert colors")
    return invert_array


def ft_red(array) -> np.ndarray:
    """Apply a red filter on the image received."""
    # Consigne : on peut utiliser les operateurs =, *
    # Pour appliquer un filtre, on va jouer sur les canaux : mettre à 0 les
    # canaux vert et bleus et/ou intensifier le canal rouge (pas nécessaire)
    red_array = np.copy(array)  # copie pour conserver l'original intact
    # on réduit les canaux Green et Blue à 0 -> filtre rouge pur
    red_array[:, :, 1] = red_array[:, :, 1] * 0  # OPERATION VECTORISEE
    red_array[:, :, 2] = red_array[:, :, 2] * 0

    ft_show_image(red_array, "Red filter")
    return red_array


def ft_green(array) -> np.ndarray:
    """Apply a green filter on the image received."""
    # Consigne : on peut utiliser les operateurs =, -.
    green_array = np.copy(array)
    # on réduit les deux autres canaux à 0 -> filtre vert pur
    green_array[:, :, 0] = green_array[:, :, 0] - green_array[:, :, 0]
    green_array[:, :, 2] = green_array[:, :, 2] - green_array[:, :, 2]

    ft_show_image(green_array, "Green filter")
    return green_array


def ft_blue(array) -> np.ndarray:
    """Apply a blue filter on the image received."""
    # Consigne : on ne peut utiliser que l'operateur =.
    blue_array = np.copy(array)
    # on réduit les deux autres canaux à 0 -> filtre bleu pur
    blue_array[:, :, 0] = 0  # Assignation a 0 avec =
    blue_array[:, :, 1] = 0

    ft_show_image(blue_array, "Blue filter")
    return blue_array


def ft_grey(array) -> np.ndarray:
    """Apply a grey filter on the image received."""
    # Consigne : on peut utiliser les operateurs =, /.
    grey_array = np.copy(array)
    # on divise chaque canal par 3
    red_channel = grey_array[:, :, 0] / 3
    green_channel = grey_array[:, :, 1] / 3
    blue_channel = grey_array[:, :, 2] / 3
    grey_final = red_channel
    grey_final = grey_final + green_channel
    grey_final = grey_final + blue_channel

    ft_show_image(grey_final, "Grayscale")
    return grey_final
