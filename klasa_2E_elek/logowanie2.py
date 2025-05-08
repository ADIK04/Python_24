login_serwer = 'marcin@onet.pl'
haslo_serwer = 'CraTA234'

zalogowano = 0
i = 1

for i in range(2):
    login_komp = input('Login: ')
    haslo_komp = input('Haslo: ')
    if login_komp == login_serwer and haslo_komp == haslo_serwer:
        print('Logowanie prawidłowe')
        zalogowano = 1
    else:
        print('Błąd logowania! Pozostało', 3 - i, 'prób')
        i += 1
