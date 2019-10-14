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

        
    def cifrarComChave(self, texto):
        texto = self.preencherPKCS5(texto)
        texto_cifrado = self.encrypt(texto)
        return texto_cifrado

    def encrypt(self, texto):
        texto_criptografado = b"".join(self.cipher.encrypt_ecb(str.encode(texto)))
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
        texto = b"".join(self.cipher.decrypt_ecb(texto_bytes)).decode()
        tamanho_padding = int(texto[len(texto) - 1])
        texto = texto[:len(texto) - tamanho_padding]
        return texto

    def decifrarComChave(self, cifra, chave):
        texto_bytes = bytes.fromhex(cifra)
        self.chave = chave
        self.cipher = blowfish.Cipher(self.chave)
        texto = b"".join(self.cipher.decrypt_ecb(texto_bytes)).decode()
        tamanho_padding = int(texto[len(texto) - 1])
        texto = texto[:len(texto) - tamanho_padding]
        return texto
        
if __name__ == "__main__":
    conversor = ConversorECB()

    # texto = input('Digite o texto para ser cifrado: ')
    # cifrado = conversor.cifrar(texto)
    # texto = conversor.decifrar(cifrado)

    # Caso 1
    textEnc1 = conversor.cifrar('FURB')
    print('CASO 1')
    print('\tCifrado -> ', textEnc1)
    print('\tQtd -> ', len(textEnc1), '\n')

    # Caso 2
    textEnc2 = conversor.cifrar('COMPUTADOR')
    print('CASO 2')
    print('\tCifrado -> ', textEnc2)
    print('\tQtd -> ', len(textEnc2))
    # Por que o texto cifrado tem tal tamanho?

    # Caso 3
    textEnc3 = conversor.cifrar('SABONETE')
    print('CASO 3')
    print('\tCifrado -> ', textEnc3)
    print('\tQtd -> ', len(textEnc3), '\n')
    # Por que o texto cifrado tem tal tamanho?

    # Caso 4
    textEnc4 = conversor.cifrar('SABONETESABONETESABONETE')
    print('CASO 4')
    print('\tCifrado -> ', textEnc4)
    print('\tQtd -> ', len(textEnc4), '\n')
    # Avalie o conteúdo do texto cifrado. Que conclusão é possível obter a partir do texto cifrado e do texto simples?
    
    # Caso 9
    textEnc9 = conversor.cifrar('FURB')
    print('CASO 9')
    print('Decifrado: ', conversor.decifrarComChave(textEnc9, b'11111'))

    # Criptografe o texto “FURB” usando o modo de operação “ECB”. A partir do texto cifrado obtido, tente  decifrá-lo utilizando a chave “11111”. Explique o resultado.
    # Reposta: Não foi possível decifrar o conteúdo