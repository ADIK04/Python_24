login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')
login_serwer = 'johnny@wp.pl'
haslo_serwer = 'CaT3rp1lla!&'

if login_komp != login_serwer and haslo_komp != haslo_serwer:
    print('Blad logowania')
elif  login_komp != login_serwer:
    print('Błedny login')
else:
    print('Logowanie poprawne')