'''Enunciado
Escreva um programa que leia do teclado um número inteiro D.
Esse número deve ser obrigatoriamente maior que zero. Em seguida,
exiba na tela todos os números inteiros menores que 100 e que sejam divisíveis por D.
'''

numero1 = int(input(' Digite um número inteiro: '))

if numero1 <= 0:

    print(' O número deve ser positivo.')

numero2 = 0

print(f' Números menores que 100, divisiveis por {numero1}')

while numero2 < 100:

    if numero2 % numero1 == 0:

        print(numero2, end= ', ')

    numero2 = numero2 + 1

print('\n Fim do programa')