import sys

# ALL(ITERABLE)
# 	built-in function that returns TRUE if all of the items of a provided iterable
# 	(List, Dictionary, Tuple, Set, etc.) are True; otherwise, it returns FALSE.

# SPLIT()
# 	The split() method splits a string into a list.
# 	You can specify the separator, default separator is any whitespace.

def main(param):
	"""
	filterstring

	Ce programme prend une string et un int, et retourne, depuis la string,
	les mots dont la taille est supérieure à int.
	"""
	string, length = param # on déploie le tuple
	words = string.split() # on divise la chaine en mots

	filtered_words = list(filter(lambda word: len(word) > length, words))
	print(filtered_words)

if __name__ == '__main__':
	try: 
		assert ( # YEAH ! On peut regrouper les assert !!
			len(sys.argv) == 3 and 										# check nb arguments
			all(c.isalpha() or c.isspace() for c in sys.argv[1]) and 	# 1er arg = chaine de char alphabetique + spaces -> LIST COMPREHENSION
			sys.argv[2].isdigit()										# 2e arg = int
		), "AssertionError: the arguments are bad"
		main((sys.argv[1], int(sys.argv[2]))) # On envoie un tuple de param (on convertit le 2ème en int)

	except AssertionError as msg:
		print(msg)
	except (KeyboardInterrupt, EOFError):
		print("\nProgram interrupted")
	except Exception as e:
		print(f"An error occurred: {e}")