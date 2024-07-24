PH = float(input(' Digite o valor PH: '))

if PH < 6:

    r = "Solução ácida"

elif PH < 7:

    r = "Solução Levemente ácida"

elif PH == 7:

    r = "Solução Neutra"

elif PH < 8:

    r = "Solução Levemente Alcalina"

else:

    r = "Solução Alcalina"

print(f' Com o PH = {PH}, é uma {r}')
