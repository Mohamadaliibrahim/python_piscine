import sys


def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


if len(sys.argv) != 2:

    print("AssertionError: more than one argument is provided")
    sys.exit(1)

arg = sys.argv[1]

if is_int(arg):

    arg = int(arg)
    if arg % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

else:

    print("AssertionError: argument is not an integer")
    sys.exit(1)
