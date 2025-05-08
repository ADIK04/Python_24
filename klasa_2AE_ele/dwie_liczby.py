'''
Napisz program który wczyta dwie różne liczby całkowite dodatnie
(np.wiek twój i najstarszej osoby w Twojej rodzinie) i 
sprawdzi ile razy mniejsza z nich mieści się w większej liczbie.
'''
liczba1 = int(input('Podaj pierwszą liczbe: '))
liczba2 = int(input('Podaj drugą liczbe: '))
if liczba1 > 0 and liczba2 > 0:
    if liczba1 >= liczba2:
        wynik = liczba1/liczba2
        print('Liczba2 miesci sie', wynik, 'w liczbie1')
    else:
        wynik = liczba2/liczba1
        print('Liczba1 miesci sie', wynik, 'w liczbie2')
else:
    print('Podano nieprawidlowe dane')
