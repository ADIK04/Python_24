login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')
login_serwer = 'johnny@wp.pl'
haslo_serwer = 'Krasz!890]'

if login_komp != login_serwer and haslo_komp != haslo_serwer:
    print('Blad logowania.')
else:
    print('Logowanie poprawne.')