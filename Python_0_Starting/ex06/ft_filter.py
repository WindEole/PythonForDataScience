import sys # import absolu et explicite
from collections.abc import Iterable # Import absolu et explicite
import ast

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

# LAMDA FUNCTION
#	A lambda function is a small anonymous function. Il can take any number of arguments,
#	but can only have one expression. Exemple : x = lambda a, b, c : a + b + c

def ft_filter(function, iterable):
	"""
	ft_filter(function or None, iterable): --> reproduit le comportement de filter()

	Construct an iterator from those elements of iterable for which function is true. 
	iterable may be either a sequence, a container which supports iteration, or an iterator. 
	If function is None, the identity function is assumed, that is, all elements of iterable
	that are false are removed.

	Note that filter(function, iterable) is equivalent to the generator expression 
	- (item for item in iterable if function(item)) -> if function is not None and 
	- (item for item in iterable if item) -> if function is None.
	"""

	if not callable(function) and function is not None:
		raise TypeError(f"{function} is not a callable function or None")
	if not isinstance(iterable, Iterable):
		raise TypeError(f"{iterable} is not an iterable")

	# NON le code ci-dessous est un générateur ! (utilise yield...)
	# for item in iterable:
	# 	if function is None:
	# 		if item:
	# 			yield item
	# 	elif function(item):
	# 		yield item

	# En List Comprehension, ça donne :
	if function is None:
		return [item for item in iterable if item]
	else: 
		return [item for item in iterable if function(item)]

def main(param=None):
	# ici on reçoit un seul paramètre, qui est un tuple. Il faut le déployer !
	function, iterable = param

	# Ensuite on envoie les arguments à la fonction ft_filter (filter() renvoie un objet de type filter, il faut le convertir en liste !)
	std_result = list(filter(function, iterable))
	print(f"Filter Standard : {std_result}")
	
	# ft_result_iter = ft_filter(function, iterable)
	ft_result = list(ft_filter(function, iterable))
	print(f"Ft_filter : {ft_result}")

if __name__ == '__main__':
	try: 
		assert len(sys.argv) == 3, f"AssertionError: two arguments required"

		# je vérifie si mon premier argument est callable ou None
		function_param = sys.argv[1]
		if function_param == "None":
			function = None
		else:
			function = eval(function_param, {"__builtins__": {}})
		assert callable(function) or function is None, f"AssertionError: le premier argument n'est pas une fonction valide ou None!"

		# je dois vérifier que mon deuxième paramètre est un iterable !
		iterable_param = sys.argv[2]
		iterable = ast.literal_eval(iterable_param)
		assert isinstance(iterable, Iterable), f"AssertionError: le 2ème argument n'est pas itérable !"

		# print("les paramètres sont valides!")
		main((function, iterable)) # On envoie les deux paramètres sous forme de tuple

	except AssertionError as msg:
		print(msg)
	except (KeyboardInterrupt, EOFError):
		print("\nProgram interrupted")
	except Exception as e:
		print(f"An error occurred: {e}")

# POUR TESTER
# cas valides :
# 	fonction lambda + list : python ./ft_filter.py "lambda x: x % 2 == 0" "[0, 1, 2, 3, 4]"
# 	fonction lambda + str : python ./ft_filter.py "lambda x: x.isupper()" "'Hello World'"
# 	fonction lambda + tuple d'entier : python ./ft_filter.py "lambda x: x > 2" "(1, 2, 3, 4)"
# 	fonction lambda + set : python ./ft_filter.py "lambda x: x < 3" "{1, 2, 3, 4}"
# 	fonction lambda + liste vide : python ./ft_filter.py "lambda x: x % 2 == 0" "[]"
# 	fonction None + liste de valeur : python ./ft_filter.py "None" "[0, 1, '', None, 3, 4, False, True]"
# cas invalides :
# 	no args : python ./ft_filter.py
# 	1er arg non callable : python ./ft_filter.py "123" "[0, 1, 2, 3, 4]"
# 	2e arg non iterable : python ./ft_filter.py "lambda x: x % 2 == 0" "123"
# 	erreur syntax dans fct : python ./ft_filter.py "lambda x: x %" "[0, 1, 2, 3, 4]"
