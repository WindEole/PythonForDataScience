import sys

# TQDM
# 	tqdm est une bibliothèque Python qui permet de créer des barres de
# 	progression pour les boucles. Il est conçu pour être facile à utiliser et
# 	à intégrer dans votre code Python existant. « tqdm » signifie « taqadum »
# 	en arabe, ce qui signifie « progresser » ou « avancer ».

# GENERATOR
# https://realpython.com/introduction-to-python-generators/
# 	Generator functions allow you to declare a function that behaves like
# 	an iterator, i.e. it can be used in a for loop. 

# YIELD 
# 	Mot clé de retour d'une fonction generator (au lieu de return)
# 	yield indicates where a value is sent back to the caller, but 
# 	unlike return, you don’t exit the function afterward.

def ft_tqdm(lst: range) -> None:
	# le code ci-dessous est un générateur ! (utilise yield...)
	for item in lst:
		yield "="

# def main(param=None)
	

# if __name__ == '__main__':
# 	try: 
# 		assert len(sys.argv) == 1, f"AssertionError: more than one argument is provided"
# 		main(sys.argv[1])
# 	except AssertionError as msg:
# 		print(msg)