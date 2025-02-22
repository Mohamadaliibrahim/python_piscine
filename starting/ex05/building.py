import sys

def check_size():
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

def is_it_punctuation(x) -> int:
    return x in ['!', '?', '.', ',', ';', ':', '-', '(', ')', '"', "'"]

def ideas_start_here():
    arg = sys.argv[1]
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
    print(f"Digits: {digit}")
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")
    print(f"Punctuation marks: {punctuation}")
    print(f"Spaces: {spaces}")
    print(f"Total characters: {counter}")

def main():
    check_size()
    ideas_start_here()

        
if __name__ == "__main__":
    main()