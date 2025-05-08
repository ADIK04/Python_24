def czy_pierwsza(liczba1):
    for i in range(2,liczba1):
        if liczba1 % i == 0:
            return 0 #False
        return 1 #True
liczba2 = int(input('Podaj liczbę: '))

if czy_pierwsza(liczba2) == 1:
    print('Liczba pierwsza')
else:
    print('Liczba złożona')