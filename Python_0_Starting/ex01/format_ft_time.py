import sys
import time

# Cet exercice sert à appréhender les modules, leur import et leur
# utilisation. Se référer aux pages biblio pour les détails sur les 
# différents fonctions

# LIBRARY TIME :

# time.time()
# 	Return the time in seconds since the epoch as a floating point number.
# 	Note that even though the time is always returned as a floating point
# 	number, not all systems provide time with a better precision than 1 
# 	second. While this function normally returns non-decreasing values, 
# 	it can return a lower value than a previous call if the system clock 
# 	has been set back between the two calls.

# time.strftime(format[, t])
# 	Convertit un n-uplet ou struct_time représentant une heure renvoyée par gmtime() ou localtime() en une chaîne spécifiée par l’argument format. 
# 	Les directives suivantes peuvent être incorporées dans la chaîne format. 
# 	%b -> Nom abrégé du mois de la région.
# 	%d -> Jour du mois sous forme décimale [01,31].
# 	%Y -> Année complète sur quatre chiffres.

# BIBLIO
# https://docs.python.org/fr/3/library/time.html#time.struct_time
# https://touron.tech/doc_info/Fiches/1-format_nombre.pdf
# https://queirozf.com/entries/python-number-formatting-examples#use-commas-as-thousands-separator

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
		# epoch = time.gmtime(0)
		# date = time.asctime(time.localtime())
		date = time.localtime()
		date_sec = time.time()				# On veut le tmps en secondes depuis epoch
		date_ns = format(date_sec, '.2e')	# On veut sa notation scientifique (format = builtin python !)
															#	|-> arrondi à 4 decimales
		print("Seconds since January 1, 1970:", "{:,}".format(round(date_sec, 4)), "or", date_ns, "in scientific notation")
												#  |-> place des virgules au milliers
		print(time.strftime("%b %d %Y"))
					# |-> formate la date