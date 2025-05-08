#Algorytm zamieniajacy Fahrenheity na Celsiusze
F = int(input('Podaj temperature w Fahrenheitach: '))
print(F, ' stopni F to ', (F - 32) * 5/9, ' stopni C.')

#Napisz algorytm zamieniajacy Celsiusze  na Fahrenheity  
C = float(input('Podaj temperature w Celsjuszach: '))
print(C, ' stopni C to ', C * 9/5 + 32, ' stopni F.')
print(type(C))
print()
print('-------------Zamiana mil na kilometry-----------')
m = float(input('Podaj mile: '))
print(m, ' mil to ', m * 1.609, ' kilometra.')
print()
print('-------------Zamiana kilometrów na mile-----------')
km = float(input('Podaj kilometry: '))
print(km, ' kilometrow to ', km / 1.609, ' mil.')