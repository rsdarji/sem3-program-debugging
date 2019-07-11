import random
import json
from random import randrange

# ======================================================================================================================
#                                              Features
# ======================================================================================================================


def encrypt(text, key):
    secret = ""
    key = int(key)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            index = (index + key) % 26
            secret += alphabet[index]
        elif char in upper_alphabet:
            index = upper_alphabet.find(char)
            index = (index + key) % 26
            secret += upper_alphabet[index]
        else:
            secret += char

    return secret


def decrypt(secret, key):
    return encrypt(secret, -int(key))


def random_key():
    return randrange(1, 26)


def random_encrypt(text):
    ...


# ======================================================================================================================
#                                           Helper Functions
# ======================================================================================================================

# If you need any helper functions, you can write them here

print(random_key())