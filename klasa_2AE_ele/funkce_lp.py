# def CzyPierwsza(liczba):
#     for i in range(2,liczba):
#         if liczba % i == 0:
#             return 0
#     return 1

# for i in range(101,1000000000,2):
#     if CzyPierwsza(i):
#         print(i, end=' ')

from math import sqrt # dołączamy moduł matematyczny(math)

def CzyPierwsza(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    
    pierwiastek = int(sqrt(n))
    for i in range(3, pierwiastek+1, 2):
        if n % i == 0:
            return 0
    return 1
# liczba = int(input('Podaj liczbę: '))

# if CzyPierwsza(liczba) == 1:
#     print('Liczba pierwsza')
# else:
#     print('Liczba złożona')

for i in range(101,1000000000,2):
    if CzyPierwsza(i):
        print(i, end=' ')
