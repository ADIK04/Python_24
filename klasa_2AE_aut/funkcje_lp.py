# def CzyPierwsza(liczba):
#     for i in range(2,liczba):
#         if liczba % i == 0:
#             return 0 
#     return 1

# liczba = int(input('Podaj liczbę: '))
# if CzyPierwsza(liczba) == 1:
#     print('Liczba pierwsza')
# else:
#     print('Liczba złożona')
def Czypierwsza(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in range(101, 100000000, 2):
    if Czypierwsza(i):
        print(i, end=' ')



