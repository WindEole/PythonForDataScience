import sys

# Assertion Error !
# Python’s assert statement allows you to write sanity checks in your code.
# These checks are known as assertions, and you can use them to test if
# certain assumptions remain true while you’re developing your code. If any
# of your assertions turn false, then you have a bug in your code.

# try et except
# 	équivalent de try/catch

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            assert (
                len(sys.argv) == 2
            ), "AssertionError: more than one argument is provided"
            try:
                num = int(sys.argv[1])
            except ValueError:
                raise AssertionError("AssertionError: argument is not an integer")
            if (num % 2) == 0:
                print("I am even")
            else:
                print("I am odd")
        except AssertionError as msg:
            print(msg)
