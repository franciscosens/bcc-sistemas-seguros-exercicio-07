import blowfish
from os import urandom

key = b'ABCDE'
blocks = 8

def encrypt(text, iv):
    cipher = blowfish.Cipher(key)
    textByte = text.encode() * blocks
    text_encrypt = b"".join(cipher.encrypt_cbc(textByte, iv))
    return text_encrypt
	
def decrypt(text_encrypt, iv):
    cipher = blowfish.Cipher(key)
    text_decrypted = b"".join(cipher.decrypt_cbc(text_encrypt, iv))
    divisor_value = int(len(text_decrypted)/blocks)
    return text_decrypted[:divisor_value];
	
# Caso 5
iv = urandom(8)
textEnc5 = encrypt('FURB', iv)
print('Cifrado -> ', textEnc5.hex())

textDec5 = decrypt(textEnc5, iv)
print('Decifrado -> ', textDec5)

# Caso 6
iv = bytes([1,1,2,2,3,3,4,4])
textEnc6 = encrypt('FURB', iv)
print('Cifrado -> ',textEnc6)

# Caso 7
iv = bytes([1,1,2,2,3,3,4,4])
textEnc7 = encrypt('SABONETESABONETESABONETE', iv)
print('Cifrado -> ', textEnc7.hex())
print('Qtd -> ', len(textEnc7.hex()))

# Caso 8
iv = bytes([10,20,30,40,50,60,70,80])
textEnc8 = encrypt('SABONETESABONETESABONETE', iv)
print('Cifrado -> ', textEnc8.hex())
print('Qtd -> ', len(textEnc8.hex()))

iv = bytes([1,1,2,2,3,3,4,4])
textDec8 = decrypt(textEnc8, iv)
print('Decifrado -> ', textDec8) 
