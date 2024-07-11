import sys

# NEW RULES:
# - Pas de scope global : def de variables tjs à l'intérieur des fonctions !
# - Main obligatoire avec __name__ == '__main__' et def main()
# - Doc obligatoire avec """Explication documentaire""", accessible avec __doc__
# - All Exception must be caught (else : fail !)
# - code at norm (norminette=flake8)

def main(param=None):
	"""building:

	This program takes a single string argument and displays the sums of its upper-case
	characters, lower-case characters, punctuation characters, digits and spaces.
	If no argument is provided, the program prompts the user to enter a string interactively.
	"""

	try: 
		if param is None:
			print("What is the text to count ?")
			inp = input(">> ")	# fct input("texte_d'amorce") pour récupérer le texte écrit sur stdin ! 
			# print(inp)
			param = inp

		i = 0
		n_lowcase = 0
		n_upcase = 0
		n_space = 0
		n_digit = 0
		n_punctuation = 0
		while i < len(param):
			if (param[i].islower()):
				n_lowcase += 1
			elif (param[i].isupper()):
				n_upcase += 1
			elif (param[i].isspace()):
				n_space += 1
			elif (param[i].isdigit()):
				n_digit += 1
			else:
				n_punctuation += 1
			i += 1

		print("The text contains", len(param), "character(s):")
		print(f"- {n_upcase} upper letter(s)")
		print(f"- {n_lowcase} lower letter(s)")
		print(f"- {n_punctuation} punctuation mark(s)")
		print(f"- {n_space} space(s)")
		print(f"- {n_digit} digit(s)")
	except KeyboardInterrupt: 		# Gestion du Ctrl + C
		print("\nKeyboard Interrupt detected. Exiting program.")
		sys.exit(1)
	except EOFError:				# Gestion du Ctrl + D
		print("\nEOFError detected. Exiting program.")
		sys.exit(1)

if __name__ == '__main__':
	try: 
		assert len(sys.argv) < 3, f"AssertionError: more than one argument is provided"
		if (len(sys.argv) < 2):
			main()
		else:
			main(sys.argv[1])
	except AssertionError as msg:
		print(msg)