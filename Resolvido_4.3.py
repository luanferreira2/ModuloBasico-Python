'''
Enunciado
Altere o programa anterior  de modo que ele continue exibindo o menor dos dois valores lidos.
 Porem, quando forem iguais o programa deve exibir
o valor junto com a mensagem " Os dois numeros são iguais"
'''

numero1 = int(input(' Digite um número inteiro: '))

numero2 = int(input(' Digite um número inteiro: '))

if numero1 < numero2:
    print(f'{numero1} é o menor dos dois números digitados.')
elif numero1 == numero2:
    print(f' {numero1}, os dois números são iguais.')
else:
    print(f'{numero2} é o menor dos dois números digitados.')