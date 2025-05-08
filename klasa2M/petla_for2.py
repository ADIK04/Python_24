
n = int(input('Podaj n: '))

suma = 0
skladnik = 2

for i in range(1,n+1):
    suma = suma + skladnik
    skladnik += 2
print('Suma', n, end='')
print(' kolejnych liczb parzystych wynosi:', suma)