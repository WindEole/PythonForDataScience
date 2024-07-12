import sys

def main(param=None):
	pass

if __name__ == '__main__':
	try: 
		assert len(sys.argv) == 3, f"AssertionError: the arguments are bad"

		# je vérifie si mon premier argument est une string -> c'est toujours le cas ! pas de check !
		# function_param = sys.argv[1]
		# if function_param == "None":
		# 	function = None
		# else:
		# 	function = eval(function_param, {"__builtins__": {}})
		# assert callable(function) or function is None, f"AssertionError: le premier argument n'est pas une fonction valide ou None!"

		# je dois vérifier que mon deuxième arg est un entier. 
		# iterable_param = sys.argv[2]
		# iterable = ast.literal_eval(iterable_param)
		# assert isinstance(iterable, Iterable), f"AssertionError: le 2ème argument n'est pas itérable !"
		assert sys.argv[2].isdigit(), f"AssertionError: Second Argument is not a number !"

		# print("les paramètres sont valides!")
		main((sys.argv[1], sys.argv[2])) # On envoie les deux paramètres sous forme de tuple

	except AssertionError as msg:
		print(msg)
	except (KeyboardInterrupt, EOFError):
		print("\nProgram interrupted")
	except Exception as e:
		print(f"An error occurred: {e}")