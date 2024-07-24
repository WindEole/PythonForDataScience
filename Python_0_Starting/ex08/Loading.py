import time
import shutil # sert pour l'affichage dynamique de la barre en fonction de la largeur de la ligne

# TQDM
# 	tqdm (taqadum en arabe, signifier progresser, ou avancer) est une bibliothèque Python
# 	qui permet de créer des barres de progression pour les boucles.

# GENERATOR
# https://realpython.com/introduction-to-python-generators/
# 	Generator functions allow you to declare a function that behaves like
# 	an iterator, i.e. it can be used in a for loop. 

# YIELD 
# 	Mot clé de retour d'une fonction generator (au lieu de return)
# 	yield indicates where a value is sent back to the caller, but 
# 	unlike return, you don’t exit the function afterward.

def format_time(seconds):
	"""
	Formatte les secondes en une chaîne de format hh:mm:ss
	"""
	return time.strftime("%M:%S", time.gmtime(seconds))

def ft_tqdm(lst: range) -> None:
	"""
	Affiche une barre de progression pour un iterable.

	Arg : un iterable de type liste (ici range)
	Yields: item -> les elements de l'iterable
	"""

	total = len(lst)
	start_time = time.time()
	fill = '█' # caractère unicode Full Block. code = U+2588
	# fill = '▓' # caractère unicode code = U+2593
	shell_width = shutil.get_terminal_size().columns # on obtient la largeur du terminal

	def print_progress(lst):
		# Gestion du temps et de la vitesse d'itération
		elapsed_time = time.time() - start_time
		elapsed_str = format_time(elapsed_time)
		estim_total_time = elapsed_time / lst * total if lst > 0 else 0
		remaining_time = estim_total_time - elapsed_time
		remaining_str = format_time(remaining_time)
		speed = lst / elapsed_time if elapsed_time > 0 else 0

		percent = f"{100 * (lst / float(total)):>3.0f}" # 3.0 => 3 char avant la virgule, comblé par des espaces, et ne pas afficher les décimales
		suffix = f"{lst:>3.0f}/{total} [{elapsed_str}<{remaining_str}, {speed:.2f}it/s]"
		# calcul de la longueur deja remplie : 
		filled_len = int((shell_width - len(percent) - len(suffix) - 4) * lst // total)
		# calcul de la longueur restante :
		bar = fill * filled_len + ' ' * ((shell_width - len(percent) - len(suffix) - 4) - filled_len)

		print(f"\r{percent}%|{bar}| {suffix}", end='\r') # 4 characteres / espaces en plus
		if lst == total:
			print()

	# Affichage initial
	print_progress(0)
	for i, item in enumerate(lst, 1):
		yield item
		print_progress(i)
	print()
