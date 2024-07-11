import sys

# object: any => le param objet peut être de n'importe quel type
# -> int => la fonction retournera un entier !

# DICTIONARY
#	https://www.w3schools.com/python/python_ref_dictionary.asp
#	methode get() = return the value of the specified key
#		dict.get(key, value) -> key is required, value optional : a value to 
#		return if the specified key does not exist. Default value None

# F-STRINGS (formatted string literals)
# 	f devant une expression => f-strings : fonctionnalité de Python qui permet 
#	d'insérer des expressions à l'intérieur de chaînes de caractères. Elles sont 
#	préfixées par la lettre f (ou F), ce qui permet d'évaluer des expressions
#	à l'intérieur des accolades {} directement dans la chaîne.

def all_thing_is_obj(object: any) -> int:
	# On doit faire une corrélation entre le type de l'object (donné par type(object))
	# et son en-tête de ligne pour affichage => dictionnaire !
	type_dict = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "String",
	}

	obj_type = type(object)
	type_name = type_dict.get(obj_type, "Type not found")
	# get va aller cherche mon obj_type dans le dictionnaire. S'il le trouve,
	# il le retourne, sinon il retourne "Type not found"
	
	if type_name != "Type not found":
		if (type_name == "String"):
			print(f"{object} is in the kitchen : {obj_type}")
		else :
			print(f"{type_name} : {obj_type}")
	else:
		print(type_name)

	return 42
