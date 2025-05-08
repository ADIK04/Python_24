login_serwer = 'Roman123'
haslo_serwer = 'Gwi@zdA#99'

zalogowano = 0
i = 1

while i <= 3 and zalogowano == 0:
    login_komp = input('Podaj login: ')
    haslo_komp = input('Podaj hasło: ')
    if login_komp == login_serwer and haslo_komp == haslo_serwer:
        print('Logowanie prawidłowe')
        zalogowano = 1
    else:
        print('Błąd logowania!', 3-i,' prób.' )
        i += 1 