'''
Escreva um programa que mostre na tela a tabuada do numero inteiro N que deve
ser lido do teclado
'''

multiplicador = 1
resultado = 1

numero = int(input(' Digite um número:'))

while multiplicador <= 10:

    resultado = numero * multiplicador

    print(f' {numero} x {multiplicador} = {resultado}')

    multiplicador = multiplicador + 1