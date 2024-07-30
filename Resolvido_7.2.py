'''
Usando a classe range, escreva um programa que leia três números inteiros:
o primeiro termo P, a razão R e a quantidade Q de termos de uma progressão aritmética.
O programa deve calcular os Q termos da progressão colocando-os em uma lista
 e no final exibi-la na tela
obs: mesmo enunciado do exercicio 7.1, porem utilizando a classe range
'''

print('\t\n Programa para progressão aritmética', end='\n\n')

p = int(input('Digite o primeiro termo: '))

r = int(input('Digite o segundo termo: '))

q = int(input('Digite a quantidade de termos: '))

ultimo = p + r * (q - 1)

termos = list(range(p, ultimo, r))

print(ultimo)

print(' Lista gerada com Range:')

print(termos)

print('\tFim do Programa')