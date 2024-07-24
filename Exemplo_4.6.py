risco = input(' Digite BX ou AL para o grau de risco: ')

valor = float(input(' Digite o valor: '))

# Lógica and para validação do risco digitado, se os dois forem verdadeiros, o programa se encerrará.
# E mostrará a Mensagem de erro.
# Se devolver falso, ele cairá no else e o resto do programa funcionará.
if risco != 'BX' and risco != 'AL':
    print(f'{risco} é invalido para o grau de risco!')
else:
    if risco == 'BX':
        if valor < 1000:
            tipo = 'Poupança'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'

    print(f'Você deve investir em {tipo}')

