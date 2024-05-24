from monoalp_encryption import cesar_cipher

def decyrpted_cesar_cipher(text, shift):
    return cesar_cipher(text, -shift)

if __name__ == '__main__':
    pass