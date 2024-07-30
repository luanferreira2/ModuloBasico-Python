'''
Escreva um enunciado que leia um número inteiro N.
Em seguida leia N números inteiros carregando os valores negativos em uma lista
e os positivos em outra. Ao final exiba na tela cada uma das listas juntamente
como seu tamanho.
obs: Se o valor zero for fornecido, ele deve ser incluído na lista de positivos.
'''

numero = int(input('Digite um número inteiro: '))

listaPosi = []

listaNeg = []

for i in range(numero):

    x = int(input(' Digite um número inteiro: '))

    if x >= 0:
        listaPosi.append(x)
    else:
        listaNeg.append(x)

print('\t Lista de números positivos')

for valor in listaPosi:

    print(valor, end=', ')

print('\n Lista de números negativos')

for valor in listaNeg:

    print(valor, end=', ')
