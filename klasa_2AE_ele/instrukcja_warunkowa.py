#INSTRUKCJA WARUNKOWA
liczba = int(input('Podaj jakas liczbe: '))
if liczba > 0:
    print('Liczba jest dodatnia')
elif liczba == 0:
    print('Liczba jest rowna zero')
else:
    print('Liczba jest ujemna')
print()




print('---------Symulacja logowania-----------')
login_serwer = 'Krzy$iu123'
haslo_serwer = '012_34-56Ab'

login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')

if login_serwer == login_komp and haslo_serwer == haslo_komp:
    print('Pomyslne logowanie!')
elif login_serwer != login_komp and haslo_serwer == haslo_komp:
    print('Bledny login')
elif haslo_serwer != haslo_komp and login_serwer == login_komp :
    print('Bledne haslo')
else:
    print('blad logowania!')



