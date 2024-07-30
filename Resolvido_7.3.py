'''
Escreva um programa que leia um número inteiro N.
 Em seguida leia N números reais carregando-os em uma lista.
  Ao final exiba os elementos da lista na tela, sendo um em cada linha.
'''

numero = int(input(' Digite um número inteiro: '))

lista = []

for i in range(numero):

    lista.append(float(input(' Digite um Número real: ')))

print('Exibição da lista:')

for valor in lista:
    print(valor)

print('\tFim do Programa')