'''
Napisz program który wczyta dwie różne liczby 
całkowite dodatnie(np.wiek twój i najstarszej 
osoby w Twojej rodzinie) i sprawdzi ile razy 
mniejsza z nich mieści się w większej liczbie.
'''
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

if liczba1 > 0 and liczba2 > 0:
    if liczba1 > liczba2:
        wynik = liczba1/liczba2
        print('Liczba2 mieści sie', wynik, 'razy w liczbie1')
    else:
        liczba2 > liczba1
        wynik = liczba2/liczba1
        print('Liczba1 mieści sie', wynik, 'razy w liczbie2')
else:
    print('Błędne dane')
