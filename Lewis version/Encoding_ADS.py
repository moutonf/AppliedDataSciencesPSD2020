from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import randrange
from webbrowser import open as open_url


def caesar_crypt(text_in, task_select="", shift=None):
    """ Text encrypter/decrypter

    Args:
        text_in: Text being encrypter/decrypter
        task_select: Selecting encrypting or decrypting
        shift: Number of shifts in the symbol line.

    Returns: Encrypter/decrypter text

    """
    # Selecting encrypter or decrypter.
    while True:
        if task_select.lower() == "e" or task_select.lower() == "d":
            task = task_select
            break
        elif task_select == "":
            task = input("Press E for encode, or D for decode: ")
            if task.lower() == "e" or task.lower() == "d":
                break
            else:
                print("\nInvalid input! Please try again!\n")

    # Selecting number of shifts.
    while True:
        try:
            if shift is None:
                shift = int(input(
                    "Please enter your shift key as an whole number: "))
            break
        except ValueError:
            print("\nInvalid input! Please try again!\n")

    if task.lower() == "e":
        pass
    elif task.lower() == "d":
        shift = -shift

    text_out_temp = []
    text_out = []
    line_text_out = ""
    crypt_value = []
    # Adding space to the symbols in punctuation
    special = " " + punctuation

    # Shifts each letter in each word according to Shift
    for line in range(len(text_in)):
        for symbol in text_in[line]:
            if symbol in ascii_uppercase:
                index = ascii_uppercase.index(symbol)
                processing = (index + shift) % 26
                crypt_value.append(processing)
                new_value = ascii_uppercase[processing]
                text_out_temp.append(new_value)

            elif symbol in ascii_lowercase:
                index = ascii_lowercase.index(symbol)
                processing = (index + shift) % 26
                crypt_value.append(processing)
                new_value = ascii_lowercase[processing]
                text_out_temp.append(new_value)

            elif symbol in digits:
                index = digits.index(symbol)
                processing = (index + shift) % 10
                crypt_value.append(processing)
                new_value = digits[processing]
                text_out_temp.append(new_value)

            elif symbol in special:
                index = special.index(symbol)
                processing = (index + shift) % 33
                crypt_value.append(processing)
                new_value = special[processing]
                text_out_temp.append(new_value)

            # Converts the list to a string.
            line_text_out = "".join(text_out_temp)

        text_out_temp.clear()
        text_out.append(line_text_out)

    # Converts the list to a string.
    text_out = "" .join(text_out)
    return text_out


random_int = randrange(26)
print("The selected c-shift is: ", random_int)

message = "Version Control System is fun"

encrypted_message = caesar_crypt(message, "E", random_int)

print("Result of encryption: ", encrypted_message)

decrypted_message = caesar_crypt(encrypted_message, "D", random_int)

print("Result of decryption: ", decrypted_message)

print("This is how to write commits.")
open_url("https://chris.beams.io/posts/git-commit/")
