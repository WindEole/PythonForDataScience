import sys

def NULL_not_found(object: any) -> int:
	list_types = ["ft_list", "ft_tuple", "ft_set", "ft_dict", "str"]
	var = str(any)
	if (var) in list_types:
		print(var, type(var))

	
	return 42 # ATTENTION ! retour 0 si succès, 1 si error

# if __name__ == '__main__':	---> PAS BESOIN
# 	if (sys.argv[0] == "./tester.py"):
# 		print(42)
