login_serwer = 'marcin@onet.pl'
haslo_serwer = 'CraTA234'
login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')
if login_serwer == login_komp and haslo_serwer == haslo_komp:
    print('Logowanie poprawne.')
elif login_komp != login_serwer:
    print('Login jest niepoprawny.')
elif haslo_komp != haslo_serwer:
    print('Hasło jest niepoprawne.')
else:
    print('Logowanie niepoprawne.')