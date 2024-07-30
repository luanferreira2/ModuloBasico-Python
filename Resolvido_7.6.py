'''
Escreva um programa que permaneça em laço lendo números inteiros.
O laço termina quando for digitado 0(zero). Cada valor diferente de zero digitado
deve ser colocado em uma lista, desde que ele ainda não esteja la, ou seja,
valores repetidos não são aceitos. Se um valor repetido por digitado, o programa deve exibir
uma mensagem na tela.
Ao final exiba a lista na tela w a quantidade de elementos que ela contem
'''

lista = []

numero = int(input(' Digite um número inteiro: '))

while numero != 0:

    if numero not in lista:
        lista.append(numero)

    else: print(f' O valor {numero} ja está na lista.')

    numero = int(input(' Digite um número inteiro: '))

for valor in lista:

    print(valor, end=', ')

print(f'\n A quantidade de elementos presentes na lista é igual a {len(lista)}')

print('\t Fim do Programa')
