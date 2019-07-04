import random
import json
import itertools

# ======================================================================================================================
#                                              Features
# ======================================================================================================================


def encrypt(text, key):
    str = ""

    for char in text:
        str = str + get_encrypt_char(char, key)
    return str

def get_encrypt_char(char, key):

    ascii_capital = range(65,91)
    ascii_small = range(97,123)
    ecncrypt_char_ascii=0
    if(ord(char) in ascii_capital):
        ecncrypt_char_ascii = ord(char)+int(key)
        if ecncrypt_char_ascii>90:
            ecncrypt_char_ascii = (ecncrypt_char_ascii%91)+65
        elif ecncrypt_char_ascii<65:
            ecncrypt_char_ascii = (ecncrypt_char_ascii%65)+26
    elif(ord(char) in ascii_small):
        ecncrypt_char_ascii = ord(char)+int(key)
        if ecncrypt_char_ascii>122:
            ecncrypt_char_ascii = (ecncrypt_char_ascii%123)+97
        elif ecncrypt_char_ascii<97:
            ecncrypt_char_ascii = (ecncrypt_char_ascii%97)+26


    else:
        return char

    return chr(ecncrypt_char_ascii)


def decrypt(secret, key):
    str = ""

    for char in secret:
        str = str + get_decrypt_char(char, key)
    return str

def get_decrypt_char(char, key):

    ascii_capital = range(65,91)
    ascii_small = range(97,123)
    deccrypt_char_ascii=0
    if(ord(char) in ascii_capital):
        deccrypt_char_ascii = ord(char)-int(key)
        if deccrypt_char_ascii>90:
            deccrypt_char_ascii = (deccrypt_char_ascii%91)+65
        elif deccrypt_char_ascii<65:
            deccrypt_char_ascii = (deccrypt_char_ascii%65)+26
    elif(ord(char) in ascii_small):
        deccrypt_char_ascii = ord(char)-int(key)
        if deccrypt_char_ascii>122:
            deccrypt_char_ascii = (deccrypt_char_ascii%123)+97
        elif deccrypt_char_ascii<97:
            deccrypt_char_ascii = (deccrypt_char_ascii%97)+26
    else:
        return char

    return chr(deccrypt_char_ascii)
def random_key():
    ...


def random_encrypt(text):
    ...


# ======================================================================================================================
#                                           Helper Functions
# ======================================================================================================================

# If you need any helper functions, you can write them here
