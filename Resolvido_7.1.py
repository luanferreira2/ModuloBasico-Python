'''
Escreva um programa que leia tres numeros inteiros: o primeiro termo P, a razão R
e a quantidade Q de termos de um progressão aritmetic. O programa deve calcular os Q
termos da progressão colocando-os em uma lista e no final exibi-la na tela
obs: exercicio ja abordado porém sem o uso de listas
'''

print('\t\n Programa para progressão aritmética', end='\n\n')

contador = 0

lista = []

p = int(input('Digite o primeiro termo: '))

r = int(input('Digite o segundo termo: '))

q = int(input('Digite a quantidade de termos: '))

while contador < q:

    lista.append(p)

    p = p + r

    contador = contador + 1


posicao = 0

# Uma maneira de mostrar a lista
print(' Lista resultante:')
print(lista)

# Usando for para imprimir a lista
for valor in lista:

    print(f' A posição numero {posicao} é igual a {valor}')
    posicao = posicao + 1

print('\t Fim do Programa')