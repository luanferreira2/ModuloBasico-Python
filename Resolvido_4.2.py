'''
Enunciado
Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois.
Se ambos forem iguais, mostrar apenas um deles
'''

numero1 = int(input(' Digite um número inteiro: '))

numero2 = int(input(' Digite um número inteiro: '))

if numero1 <= numero2:
    print(f'{numero1} é o menor dos dois números digitados.')
else:
    print(f'{numero2} é o menor dos dois números digitados.')