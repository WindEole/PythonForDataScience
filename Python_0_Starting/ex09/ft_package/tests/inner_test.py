from ft_package.count_lines import count_lines_in_file

def test_count_lines_in_file():
	test_file_path = "test_file.txt"

	# on écrit quelques lignes dans un fichier de test temporaire
	with open(test_file_path, "w") as test_file:
		test_file.write("First line\nSecond line\nThird line\n")
	
	num_lines = count_lines_in_file(test_file_path)
	expected_num_lines = 3
	
	print(f"Number of lines: {num_lines}")
	assert num_lines == expected_num_lines, f"Expected {expected_num_lines} lines, but got {num_lines}"

	# on supprime le fichier de test
	import os
	os.remove(test_file_path)

if __name__ == "__main__":
	test_count_lines_in_file()
	print("All tests passed.")