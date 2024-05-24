from monoalp_encryption import cesar_cipher
from monoalp_decryption import decyrpted_cesar_cipher
from monoalp_encryption import random_key_shift


def test():
    with open(r"text english", "r", encoding="utf8") as f:
        text = f.read()

        key_shift = random_key_shift()
        print(f"Random Key Shift: {key_shift}")
        encrypted_text = cesar_cipher(text, key_shift)
        decrypted_text = decyrpted_cesar_cipher(encrypted_text, key_shift) 
        print('This is encrypted text')
        print('-------------------------------')
        print (f'{encrypted_text}')
        print('This is decrypted text')
        print('-------------------------------')
        print (f'{decrypted_text}')

test()