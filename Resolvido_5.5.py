'''
Enunciado
Escreva um programa que permaneça em laço enquanto o valor digitado
for diferente de zero. Totalize e conte os valores digitados, exceto o zero,
e apresente esses valores na tela.
'''

soma = 0

numero = 1

contador = 0

while numero != 0:

    numero = int(input(' Digite um número inteiro: '))

    soma = soma + numero

    if numero != 0:

        contador = contador + 1

print(f' A soma dos {contador} numeros é igual a {soma}')
