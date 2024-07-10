import sys

# Cet exercice sert à appréhender les list / set / tuple / dict en python,
# et voir les opérations qu'on peut faire ou non, et comment contourner ce
# que l'on ne peut pas faire... 

# BIBLIO
# https://koor.fr/Python/Tutorial/python_type_set.wp#parcours
# https://waytolearnx.com/2019/04/convertir-une-liste-en-tuple-python.html
# https://www.docstring.fr/glossaire/tuple/
# https://www.w3schools.com/python/python_dictionaries.asp

class color:
	GRAY = '\033[90m'		# ------ GRIS -------- #
	REALGRAY = '\033[38;2;128;128;128m'
	SILVER = '\033[38;2;192;192;192m'
	LIGHTSLATEGRAY = '\033[38;2;119;136;153m'
	RED = '\033[91m'		# ------ ROUGE ------- #
	ORANGE = '\033[38;2;255;165;0m'
	FIREBRICK = '\033[38;2;178;34;34m'
	INDIANRED = '\033[38;2;205;92;92m'
	GREEN = '\033[92m'		# ------ VERT -------- #
	LIMEGREEN = '\033[38;2;50;205;50m'
	FORESTGREEN = '\033[38;2;34;139;34m'
	SPRINGGREEN = '\033[38;2;0;255;127m'
	YELLOW = '\033[93m'		# ------ JAUNE ------- #
	KHAKI = '\033[38;2;240;230;140m'
	REALYELLOW = '\033[38;2;255;255;0m'
	GOLD = '\033[38;2;255;215;0m'
	BLUE = '\033[94m'		# ------ BLEU -------- #
	REALBLUE = '\033[38;2;0;0;255m'
	DEEPSKYBLUE = '\033[38;2;0;191;255m'
	ROYALBLUE = '\033[38;2;65;105;225m'
	PURPLE = '\033[95m'		# ------ VIOLET ------ #
	FUCHSIA = '\033[38;2;255;0;255m'
	DARKVIOLET = '\033[38;2;148;0;211m'
	DARKMAGENTA = '\033[38;2;139;0;139m'
	CYAN = '\033[96m'		# ------ CYAN -------- #
	AQUAMARINE = '\033[38;2;127;255;212m'
	PALETURQUOISE = '\033[38;2;175;238;238m'
	TEAL = '\033[38;2;0;128;128m'
	RESET = '\033[0m'		# ------ RESET ------- #

if __name__ == '__main__':
	if (len(sys.argv) != 1):
		print(color.FIREBRICK + "Check Arguments" + color.RESET)
	else:
		ft_list = ["Hello", "tata!"]
		ft_tuple = ("Hello", "toto!")
		ft_set = {"Hello", "tutu!"}
		ft_dict = {"Hello" : "titi!"}

		# pour une liste [elm1, elm2], les elements sont accessible et changeable via leur indice !
		ft_list[1] = "World!"

		# pour un tuple (elm1, elm2) : liste immuable, non mutable. On ne peut ni ajouter ni changer une des valeurs. 
		# on peut juste convertir le tuple en list, modifier la valeur, puis reconvertir en tuple
		tuple_to_list = list(ft_tuple)
		tuple_to_list[1] = "France!"
		ft_tuple = tuple(tuple_to_list)

		# SET : on peut l'initialiser soit avec la fonction set(), soit avec les accolades {}
		# Les valeurs d'un set {elm1, elm2} sont inchangeable, il faut remove puis add un element !
		# ft_set.clear()
		# ft_set.add("Hello")
		ft_set.remove("tutu!")
		ft_set.add("Paris!")

		# dans un dict {key:value} ordered and changeable and no duplicate
		ft_dict["Hello"] = "42Paris!"

		print(ft_list)
		print(ft_tuple)
		print(ft_set)
		print(ft_dict)