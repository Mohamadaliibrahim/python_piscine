import sys

def the_exception():
    arg = input("What is the text to count?\n")
    ideas_start_here(arg)

def check_size() -> bool:
    if len(sys.argv) == 1:
        the_exception()
        return (False)
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    return (True)

def is_it_punctuation(x) -> bool:
    return x in ['!', '?', '.', ',', ';', ':', '-', '(', ')', '"', "'", '/', '\\']

def ideas_start_here(arg):
    i = 0
    digit = 0
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    counter = 0
    while i < len(arg):
        if arg[i].isdigit():
            digit += 1
        elif arg[i].isupper():
            upper += 1
        elif arg[i].islower():
            lower += 1
        elif is_it_punctuation(arg[i]):
            punctuation += 1
        elif arg[i] == ' ':
            spaces += 1
        counter += 1
        i +=1
    print(f"The text containes {counter} characters: ")
    print(f"{upper} uppercase letters")
    print(f"{lower} lowercase letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")

def main():
    if check_size():
        ideas_start_here(sys.argv[1])

        
if __name__ == "__main__":
    main()