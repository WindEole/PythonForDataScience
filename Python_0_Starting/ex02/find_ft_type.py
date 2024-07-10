import sys

def all_thing_is_obj(object: any) -> int:
	list_types = ["ft_list", "ft_tuple", "ft_set", "ft_dict", "str"]
	var = str(any)
	if (var) in list_types:
		print(var, type(var))

	
	return 42

# if __name__ == '__main__':	---> PAS BESOIN
# 	if (sys.argv[0] == "./tester.py"):
# 		print(42)
