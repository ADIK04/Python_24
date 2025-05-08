# Instrukcja warunkowa
liczba = int(input('Podaj liczbę: '))
if liczba > 0:
    print('Liczba jest dodatnia.') 
elif liczba == 0:
    print('Liczba jest zerem.') 
else:
    print('Liczba jest ujemna.') 

# +++++++++++++++++++++++++++++++++++++++++++++
print('++++++++++SYMULACJA LOGOWANIA+++++++++++')
login_serwer = 'rysiek@onet.pl'
haslo_serwer = 'M@ryLA16'
login_komp = input('Podaj login: ')
haslo_komp = input('Podaj haslo: ')

if login_komp != login_serwer and haslo_komp == haslo_serwer:
    print('Logowanie jest poprawne.')
else:
    print('Logowanie jest bledne.')



    