'''
Escreva um programa que permaneça em laço lendo números inteiros.
O laço termina quando for digitado 0(zero). Cada valor diferente de zero digitado
deve ser colocado em uma lista. Ao final exiba a lista na tela w a quantidade de elementos que
ela contem
'''

numero = 1

lista = []

while numero != 0:

    numero = int(input(' Digite um número inteiro: '))

    if numero == 0:

        break

    else:

        lista.append(numero)

for valor in lista:

    print(valor, end=', ')

print(f'\n A quantidade de elementos presentes na lista é igual a {len(lista)}')

print('\t Fim do Programa')
