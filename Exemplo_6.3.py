''' Tratamento de Exceções'''
try:
    a = int(input(' Digite o valor de A: '))
    b = int(input(' Digite o valor de B: '))

    r = a / b
    print(r)

except ZeroDivisionError:
    print(' O valor de B não pode ser zero')
except ValueError:
    print(' Digite corretamente os número inteiros para A e B.')
except:
    print(' Impossível realizar a divisão')

print(' Fim do Programa')