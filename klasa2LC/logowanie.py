print('++++++++Symulacja logowania+++++++++++')
login_serwer = 'marian@onet.pl'
haslo_serwer = 'zag!EL<9'
login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')

if login_serwer != login_komp and haslo_komp != haslo_serwer:
    print('Niepoprawne login i haslo.')
elif login_serwer != login_komp:
    print('Niepoprawny login.')
elif haslo_komp != haslo_serwer:
    print('Niepoprawny haslo.')
else:
    print('Logowanie poprawne')

