import blowfish
from os import urandom

class ConversorECB:
    def __init__(self):
        self.chave = b"ABCDE"
        self.cipher = blowfish.Cipher(self.chave)
        self.iv = urandom(8)

    def cifrar(self, texto):
        texto = self.preencherPKCS5(texto)
        texto_cifrado = self.encrypt(texto)
        return texto_cifrado

    def encrypt(self, texto):
        texto_criptografado = b"".join(self.cipher.encrypt_ecb_cts(str.encode(texto)))
        return texto_criptografado.hex()

    def calcular_quantidade_blocos(self, texto):
        texto_tamanho = len(texto)
        resto = texto_tamanho % 8
        return resto

    def preencherPKCS5(self, texto):
        resto = self.calcular_quantidade_blocos(texto)
        tamanho_padding = 8

        if resto != 0:
            tamanho_padding = 8 - resto
        texto_preenchido = texto
        for i in range(tamanho_padding):
            texto_preenchido = texto_preenchido + str(tamanho_padding)

        return texto_preenchido

    def decifrar(self, cifra):
        texto_bytes = bytes.fromhex(cifra)
        print(texto_bytes)
        texto = b"".join(self.cipher.decrypt_ecb_cts(texto_bytes)).decode()
        tamanho_padding = int(texto[len(texto) - 1])
        texto = texto[:len(texto) - tamanho_padding]
        return texto
        

if __name__ == "__main__":
    conversor = ConversorECB()

    texto = input('Digite o texto para ser cifrado: ')
    cifrado = conversor.cifrar(texto)
    texto = conversor.decifrar(cifrado)
    print(cifrado)
    print(texto)
