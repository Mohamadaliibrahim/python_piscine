import sys
import re

morse_code_dict ={
    'a': '.-',      'b': '-...',    'c': '-.-.',    'd': '-..',     'e': '.',  
    'f': '..-.',    'g': '--.',     'h': '....',    'i': '..',      'j': '.---',  
    'k': '-.-',     'l': '.-..',    'm': '--',      'n': '-.',      'o': '---',  
    'p': '.--.',    'q': '--.-',    'r': '.-.',     's': '...',    't': '-',    
    'u': '..-',     'v': '...-',   'w': '.--',     'x': '-..-',    'y': '-.--',  
    'z': '--..',    '1': '.----',   '2': '..---',   '3': '...--',  '4': '....-', 
    '5': '.....',   '6': '-....',   '7': '--...',   '8': '---..',  '9': '----.', 
    '0': '-----',   ' ': '/',       'A': '.-',      'B': '-...',    'C': '-.-.',
    'D': '-..',     'E': '.',       'F': '..-.',    'G': '--.',     'H': '....',
    'I': '..',      'J': '.---',    'K': '-.-',     'L': '.-..',    'M': '--',
    'N': '-.',      'O': '---',     'P': '.--.',    'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',        'U': '..-',     'V': '...-',   'W': '.--',
    'X': '-..-',    'Y': '-.--',    'Z': '--..'
}

def text_to_morse(text):
    morse_code = []
    for index in text:
        if index in morse_code_dict:
            morse_code.append(morse_code_dict[index])
    return ' '.join(morse_code)

def check_args():
    av = sys.argv
    if len(av) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if  not isinstance(av[1], str):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not re.match(r'^[a-zA-Z0-9.-/ ]*$', av[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if '  ' in av[1]:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

def main():
    check_args()
    av = sys.argv
    print(text_to_morse(av[1]))


if __name__ == "__main__":
    main()