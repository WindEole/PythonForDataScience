import sys
from collections.abc import Iterable

# NEW RULES:
# - Pas de scope global : def de variables tjs à l'intérieur des fonctions !
# - Main obligatoire avec __name__ == '__main__' et def main()
# - Doc obligatoire avec """Explication documentaire""", accessible avec __doc__
# - All Exception must be caught (else : fail !)
# - code at norm (norminette=flake8)

# FILTER(function, iterable) Builtin fct
#	Construct an iterator from those elements of iterable for which function is true. 
#	iterable may be either a sequence, a container which supports iteration, or an 
#	iterator. If function is None, the identity function is assumed, that is, all 
#	elements of iterable that are false are removed.

# ITERABLE
#	En python, un itérable est un objet qui peut par exemple être utilisé dans une
#	boucle for. Cela signifie que vous pouvez parcourir chaque élément de l’itérable
#	un par un et effectuer une action sur chacun d’eux.
#		listes
#		tuples
#		chaînes de caractères
#		objets range()
#	Pour savoir si un objet est itérable en Python, vous pouvez utiliser la fonction
#	iter() intégrée. Cette fonction prend un objet en argument et retourne un objet
#	itérateur s’il est itérable, ou une exception TypeError s’il n’est pas itérable.

# LIST COMPREHENSION
#	List comprehension offers a shorter syntax when you want to create a new list
#	based on the values of an existing list. Exemple : 
#		fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#		newlist = [x for x in fruits if "a" in x]
#		print(newlist) -> une nouvelle liste est créée avec des conditions

def ft_filter(function, iterable):
	"""
	ft_filter(function or None, iterable): --> reproduit le comportement de filter()

	Construct an iterator from those elements of iterable for which function is true. 
	iterable may be either a sequence, a container which supports iteration, or an iterator. 
	If function is None, the identity function is assumed, that is, all elements of iterable
	that are false are removed.

	Note that filter(function, iterable) is equivalent to the generator expression 
	- (item for item in iterable if function(item)) if function is not None and 
	- (item for item in iterable if item) if function is None.
	"""
	pass

def main(param=None):

	# pass
	# print(filter.__doc__)
	print(ft_filter.__doc__)

if __name__ == '__main__':
	# VERIF DES PARAMETRES !
	print(len(sys.argv))
	try: 
		assert len(sys.argv) > 2, f"AssertionError: check the arguments provided"

		# je vérifie si mon premier argument est callable ou None
		function_param = sys.argv[1]
		if function_param == "None":
			function = None
		else:
			function = eval(function_param)
		assert callable(function) or function is None, f"AssertionError: le premier argument n'est pas une fonction valide ou None!"

		# je dois vérifier que mon deuxième paramètre est un iterable !
		iterable = sys.argv[2]
		# iterable = eval(iterable_param)
		assert isinstance(iterable, Iterable), f"AssertionError: le 2ème argument n'est pas itérable !"

		print("les paramètres sont valides!")
		main((function, iterable))

	except AssertionError as msg:
		print(msg)

	# try: 
	# 	assert len(sys.argv) < 3, f"AssertionError: more than one argument is provided"
	# 	if (len(sys.argv) < 2):
	# 		main()
	# 	else:
	# 		main(sys.argv[1])
	# except AssertionError as msg:
	# 	print(msg)