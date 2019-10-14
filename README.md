# Desenvolvimento de Sistemas Seguros - Exercício 07

Fundação da Universidade Regional de Blumenau

Alunos: 
* Francisco Lucas Sens
* Gabriel Castellani de Oliveira

[Conteúdo](assets/TiposDeCifragem.pdf)

# Enunciado: 

Nesta lista, iremos exercitar a utilização de um algoritmo de criptografia.

Utilizaremos o algoritmo “Blowfish”. Este algoritmo utiliza cifragem de bloco de 64 bits. Nestes exercícios, utilize o esquema de preenchimento de bloco “PKCS#5” para todos os casos desta lista. Utilize também como chave a sequência de caracteres “ABCDE”.

Crie um programa para as questões abaixo. Submeta no AVA o programa que você construiu, bem como as respostas às
perguntas das questões abaixo:

## Caso 1

Criptografe o texto “FURB” usando o modo de operação “ECB”.

1.1. Qual o conteúdo do texto cifrado (em hexadecimal)?

1.2. Qual a extensão (quantidade de caracteres) do texto cifrado?

## Caso 2

Criptografe “COMPUTADOR” e o modo de operação “ECB”.

2.1. Qual o conteúdo do texto cifrado (em hexadecimal)?

2.2. Qual a extensão do texto cifrado?

2.3. Por que o texto cifrado tem tal tamanho?

## Caso 3

Criptografe “SABONETE” e utilize o modo de operação “ECB”.

3.1. Qual o conteúdo do texto cifrado (em hexadecimal)?

3.2. Qual a extensão do texto cifrado?

3.3. Por que o texto cifrado tem tal tamanho?

## Caso 4

Criptografe o texto “SABONETESABONETESABONETE” e utilize o modo de operação “ECB”.

4.1. Qual o conteúdo do texto cifrado (em hexadecimal)?

4.2. Qual a extensão do texto cifrado?

4.3. Avalie o conteúdo do texto cifrado. Que conclusão é possível obter a partir do texto cifrado e do texto simples?

## Caso 5

Criptografe o texto “FURB” e agora utilize o modo de operação “CBC”.

5.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
Cifrado ->  f545d3b8539a04049a6c82f7fdc5c2b1573eb74cf127cc9dc07afa897f826972

5.2. Tente decifrar o texto cifrado, para recuperar o texto simples. O que acontece?
Decifrado ->  b'FURB'

## Caso 6

Criptografe o texto “FURB”, utilizando o modo de operação “CBC”. Estabeleça que o vetor de inicialização seja constituído dos bytes: 1, 1, 2, 2, 3, 3, 4, 4.

6.1. Qual o conteúdo do texto cifrado?
Cifrado ->  b'\x13e\xdc\xcdq.$\x03\x8e(Q\xcc\xca\x9du\xce\x94\xf3\xa7\x89\x91g\xf5x\xaa \x86\xf5\xf47\xf8\x01'

## Caso 7

Criptografe o texto “SABONETESABONETESABONETE” e utilize o modo de operação “CBC”. Defina o vetor de inicialização constituído dos bytes 1, 1, 2, 2, 3, 3, 4, 4.

7.1. Qual o conteúdo do texto cifrado (em hexadecimal)?

Cifrado ->  9b1813dacaf2d6509d10c55c33f36b0918d49bf6cd0c12414040498c1034ca9b3a7f56cd3257bd7c3a6d8b48706107c4ece6ea5603b60dd966c2a7f97a1840ae9fb7dafa1d1152d5213eddc00a36436c930547a086428a489f92593232d4e0255f3f8ded06d11f63e5b2fba22f2f543302e176d936a21ab36462ab119f27461b116b54d5513e8a161bf014cf382d758e5678be9c31f9fe56d6cb73f962fd5b298ffa9cb6b5bf52dc994d8e7fad140149b2b4c9690f519611a41bc296c7d1c409
Qtd ->  384

7.2. Compare o texto cifrado com aquele obtido no caso 4 e apresente uma conclusão desta comparação.

## Caso 8

Criptografe o texto “SABONETESABONETESABONETE” e utilize o modo de operação “CBC”. Defina o vetor de inicialização constituído dos bytes 10,20,30,40,50,60,70,80.

8.1. Qual o conteúdo do texto cifrado?
Cifrado ->  10981fe3009f1fe0ab7592179c361cc7af8eb390b79ebc8e226bf5bdde1dd415488267dbd0424593dfa8593f013360c72d496baef78228902bb6512c210e3f28154610643c883016b3d7c83a8533d188ac0804c9b149149c15f4a91788732195d9189bb00d35a2414bdd340088a93262441836a48fd08c694332a2ccd8012b3d3d0718174c75ffe75a1f61075c5f99ff378eb0375da47139378cf96cf923d04271378870bd5bb52ef3292134f9d37ffbf62919ce344e144315f70044db5a41ec
Qtd ->  384

8.2. Compare o texto cifrado com o que foi obtido no caso 7 e apresente conclusão sobre a comparação.
Os dois textos cifrados possuem a mesma quantidade de bytes

8.3. A partir do resultado de 8.2, decriptografe a mensagem usando o vetor de inicialização constituído dos bytes 1, 1, 2, 2, 3, 3, 4, 4. Qual a conclusão que você atinge?
Decifrado ->  b'XT^e\x7fz\x16\x11SABONETESABONETE'
Utilizando um vetor de bytes diferente do primeiro, não é possível decifrar o texto por completo

## Caso 9

9.1. Criptografe o texto “FURB” usando o modo de operação “ECB”. A partir do texto cifrado obtido, tente decifrá-lo utilizando a chave “11111”. Explique o resultado.