import sys
from ft_filter import ft_filter

# methode ALL(ITERABLE)
# 	built-in function that returns TRUE if all of the items of an iterable
# 	(List, Dictionary, Tuple, Set, etc.) are True; otherwise, it returns FALSE.

# methode SPLIT()
# 	The split() method splits a string into a list.
# 	You can specify the separator, default separator is any whitespace.


def main(param):
    """Return words whose size is superior than int.

    Filterstring est un programme qui prend une string et un int, et retourne,
    depuis la string, les mots dont la taille est supérieure à int.
    """
    string, length = param  # on déploie le tuple
    words = string.split()  # on divise la chaine en mots

    filtered_words = list(ft_filter(lambda word: len(word) > length, words))
    print(filtered_words)


if __name__ == "__main__":
    try:  # YEAH ! On peut regrouper les assert !!
        assert (
            len(sys.argv) == 3  # check nb arguments
            and all(c.isalpha() or c.isspace() for c in sys.argv[1])
            # 1er arg = chaine de char alpha + spaces -> LIST COMPREHENSION
            and sys.argv[2].isdigit()  # 2e arg = int
        ), "AssertionError: the arguments are bad"
        main((sys.argv[1], int(sys.argv[2])))
        # On envoie un tuple de param (on convertit le 2ème en int)

    except AssertionError as msg:
        print(msg)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted")
    except Exception as e:
        print(f"An error occurred: {e}")
