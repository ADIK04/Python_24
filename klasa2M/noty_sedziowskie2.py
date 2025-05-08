print('wprowadz noty za skok: ')
nota = float(input())
minimalna = nota
maksymalna = nota
suma = 0

while nota != 0: 
    suma += nota # suma = suma + nota
    if nota < minimalna:
        minimalna = nota
    if nota > maksymalna:
        maksymalna = nota
    nota = float(input())
suma = suma-minimalna-maksymalna
print('\nNoty skrajne: ', minimalna, ' i ', maksymalna)
print('Łączna nota: ', suma)