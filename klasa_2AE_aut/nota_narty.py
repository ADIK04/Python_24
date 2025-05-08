print('Wprowadz noty za skok: ')
nota = float(input())
najmniejsza = nota
najwieksza = nota
suma = nota

for i in range(4):
    nota = float(input())
    suma += nota
    if nota < najmniejsza:
        najmniejsza = nota
    if nota > najwieksza:
        najwieksza = nota
suma = suma-najmniejsza-najwieksza
