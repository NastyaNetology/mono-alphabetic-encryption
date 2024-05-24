import random

def random_key_shift():
    return random.randint(1, 25)


def cesar_cipher(text, shift):
    encyrpted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                ascii_code = ord(char) #return the ascii code for char
                shifted_code = (ascii_code - 97 + shift) % 26 + 97 #normalize the lower char's code from 0 to 25 instead of 97 to 122
            elif char.isupper():
                ascii_code = ord(char)
                shifted_code = (ascii_code - 65 + shift) % 26 + 65 #normalize the upper char's code from 0 to 25 instead of 65 to 90
            encyrpted_text += chr(shifted_code) #returns a string where char's ascii_code was shifted
                
        else:
            encyrpted_text += char
    return encyrpted_text


if __name__ == '__main__':
    pass