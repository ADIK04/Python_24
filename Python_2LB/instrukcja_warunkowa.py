liczba = int(input('Podaj jakąś liczbę: '))
if liczba > 0: # pierwszy warunek, zawsze zaczyna się od if
    print('Liczba jest dodatnia.') # po dwukropku, kolejna linia ma wcięcie
elif liczba == 0:# drugi i kolejny warunek,  zaczyna się od elif
    print('Liczba jest równa zero.')
else: # w innym  wypadku
    print('Liczba jest ujemna.')
#############################################
#########SYMULACJA LOGOWANIA NA SERWERZE##########################
print()
print('SYMULACJA LOGOWANIA NA SERWERZE')
login_serwer = 'andrzEJ8'
haslo_serwer = '$zcz3N@89'
login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')
if login_komp == login_serwer and haslo_komp == haslo_serwer:
    print('Logowanie prawidłowe.')
else:
    print('Błąd logowania.')