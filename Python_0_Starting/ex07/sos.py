import sys

# JOIN()
# 	The join() method takes all items in an iterable and joins them into one string.
# 	A string must be specified as the separator.

def convert_to_morse(param):
	"""
	Convertit une chaine alphanumerique en code Morse'

	Args	= param (string) : la chaine à convertir
	Return	= string : la chaine convertie en morse
	"""

	NESTED_MORSE = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	".": ".-.-.-",
	",": "--..--",
	"?": "..--..",
	" ": "/",
	}

	morse = [NESTED_MORSE.get(c.upper(), '') for c in param]
	return ' '.join(morse)

def main(param=None):
	if param is None:
		print("Please provide a string to convert to Morse code.")
		return
	morse = convert_to_morse(param)
	print(morse)

if __name__ == '__main__':
	try: 
		assert ( # YEAH ! On peut regrouper les assert !!
			len(sys.argv) == 2 and 									# check nb arguments
			all(c.isalnum() or c.isspace() for c in sys.argv[1]) 	# 1er arg = chaine alphanumerique + spaces -> LIST COMPREHENSION
		), "AssertionError: the arguments are bad"
		main(sys.argv[1])

	except AssertionError as msg:
		print(msg)
	except (KeyboardInterrupt, EOFError):
		print("\nProgram interrupted")
	except Exception as e:
		print(f"An error occurred: {e}")