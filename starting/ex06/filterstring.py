import sys
import ft_filter

def check_input():
    av = sys.argv
    z = ['!', '?', '.', ',', ';', ':', '-', '(', ')', '"', "'", '/', '\\']
    if len(av) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    x = av[1]
    if  not isinstance(av[1], str):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not av[2].isdigit():
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if any(ft_filter.ft_filter(lambda x: x in z, av[1])):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

def filter_the_words(words, length):
    return [word for word in words if len(word) > length]
    

def ideas_start_here():
    av = sys.argv
    words = av[1].split()
    length = int(av[2])
    result = filter_the_words(words, length)
    print (result)
    
    

def main():
    check_input()
    ideas_start_here()
    

if __name__ == "__main__":
    main()