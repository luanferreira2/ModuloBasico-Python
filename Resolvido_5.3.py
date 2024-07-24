'''
 Enunciado
Escreva um programa que mostre na tela os 10 primeiros termos de um progressão aritmética (PA)
com primeiro termo P e razão R.
Os dois números P e R são inteiros e devem ser lidos do teclado.
'''

p = int(input('Digite o primeiro termo: '))

r = int(input('Digite o segundo termo: '))

contador = 0

print(f'Termo "um" digitado: {p}')

print(f'Termo "dois" digitado: {r}')

while contador < 10:

    print(p, end = ', ')

    p = p + r

    contador = contador + 1

print('\n Fim do Programa.')

