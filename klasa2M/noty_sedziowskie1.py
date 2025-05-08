print('wprowadz noty za skok: ')
nota = float(input())
minimalna = nota
maksymalna = nota
suma = nota

for i in range(4):
    nota = float(input())
    suma += nota # suma = suma + nota
    if nota < minimalna:
        minimalna = nota
    if nota > maksymalna:
        maksymalna = nota
suma = suma-minimalna-maksymalna
print('\nNoty skrajne: ', minimalna, ' i ', maksymalna)
print('Łączna nota: ', suma)