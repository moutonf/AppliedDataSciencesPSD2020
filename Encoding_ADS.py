# V1.1 Encoding ADS
# Original author Leon Helgeland

import random  # Import random library

string = "Version control system is fun"  # String to encrypt
shift = random.randint(0, 26)  # Randomly selects an integer between 0 and 26

def uncrypt(x):  # Unencodes the string
    unencoded_string = ""  # Variable that has new shifted letters appended to it to form the complete string
    for i in x:  # Loops through each letter of the string
        unencoded_string += chr(ord(i) - shift)  # Uses the integer we got from random to shift the letters accordingly

    print(f"\nUnencoding string using caesar cipher shifting the letters {shift} times backward.\nString to unencode: {x}\nUnencoded string: {unencoded_string}")


def ceasar_chipher():  # Encodes the string
    encoded_string = ""  # Variable that has new shifted letters appended to it to form the complete string
    for i in string:  # Loops through each letter of the string
        encoded_string += chr(ord(i) + shift)  # Uses the integer we got from random to shift the letters accordingly

    print(f"Encoding string using caesar cipher shifting the letters {shift} times forward.\nString to encode: {string}\nEncoded string: {encoded_string}")
    uncrypt(encoded_string)  # Calls the unencoding function

ceasar_chipher() # Calls the caesar_cipher function

