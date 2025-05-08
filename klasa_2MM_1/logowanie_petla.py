login_serwer = 'johnny@wp.pl'
haslo_serwer = 'CaT3rp1lla!&'

zalogowano = 0
i = 1
while i <= 3 and zalogowano == 0:
    login_komp = input('Login: ')
    haslo_komp = input('Haslo: ')
    if login_komp == login_serwer and haslo_komp == haslo_serwer:
        print('Logowanie prawidlowe')
        zalogowano = 1
    else:
        print('Błąd logowania! Pozostalo', 3- i,'prób')
        i +=1 