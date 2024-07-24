'''
Escreva um programa que permaneça em laço enquanto um valor de X lido for diferente de zero.
Para cada Valor de X apresentar se ele é par ou impar.
'''

x = 1

while x != 0:

    x = int(input(' Digite um valor para X: '))

    print('', x)

    if x % 2 == 0:

        print(' Este número é par.')

    else:

        print(' Este número é impar.')

print('Fim do programa.')
