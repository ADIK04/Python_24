print('++++++++++++++++SYMULACJA LOGOWANIA+++++++++++')
login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')
login_serwer = 'janusz@wp.pl'
haslo_serwer = 'And5zej!'
# Uaktulanij powyższy kod,aby otrzymywać komunikat 'Niepoprawne hasło'
# 'Niepoprawny login'
if login_komp != login_serwer and haslo_komp != haslo_serwer:
    print('Logowanie jest niepoprawne.') 
elif login_komp != login_serwer:
    print('Login jest niepoprawny.')
elif haslo_komp != haslo_serwer:
    print('Haslo jest niepoprawne')
else:
    print('Logowanie poprawne!!!')


