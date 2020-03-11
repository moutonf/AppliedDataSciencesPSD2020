import random

text = 'Version Control is fun.'
shift_random = random.randint(0, 26)


def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char.islower():
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 32) % 26 + 32)
    return cipher


def decrypt(string, shift):
    cipher = ''
    for char in string:
        if char.islower():
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 32) % 26 + 32)
    return cipher


encrypted_text = encrypt(text, shift_random)
decrypted_text = decrypt(encrypted_text, shift_random)
print(encrypted_text)
print(decrypted_text)
