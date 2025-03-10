import sys
import re


def text_to_morse(text):
    """
    Converts a given text to Morse code.
    Args:
        text (str): The text to convert to Morse code.
    Returns:
        str: The Morse code representation of the input text.
    """
    morse_code_dict = {
        'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
        'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
        'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
        'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',  't': '-',
        'u': '..-',   'v': '...-', 'w': '.--', 'x': '-..-',  'y': '-.--',
        'z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/',
        }
    morse_code = []
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
    return ' '.join(morse_code)


def check_args():
    """
    Validates command-line arguments.
    Exits the program with an error message if arguments are invalid.
    """
    av = sys.argv
    if len(av) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not re.match(r'^[a-zA-Z0-9.-/ ]*$', av[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if '  ' in av[1]:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


def main():
    """Main function to check arguments and convert text to Morse code."""
    check_args()
    av = sys.argv
    print(text_to_morse(av[1]))


if __name__ == "__main__":
    main()
