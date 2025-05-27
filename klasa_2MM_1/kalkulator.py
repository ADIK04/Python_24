#---------------------KALKULATOR----------------------
#.....................I.Funkcje.........................
def dodawanie(a,b):
    return a + b
#.....................II.Menu............................
print('Podaj działanie: ')
print('1.Dodawanie')
# Uzupełnij menu o pozostałe nazwy działan: odejmowanie,mnożenie,
#  dzielenie, potęgowanie, reszta z dzielenia, pierwiastkowanie,potegowanie

#.....................III.Wyliczenia(logika)......................
wybor = input('Podaj działanie które chcesz wykonac: ')
if wybor == '1':
    liczba1 = int(input('Podaj pierwszą liczbę: '))
    liczba2 = int(input('Podaj drugą liczbę: '))
    if wybor == '1':
        print(liczba1, '+', liczba2, '=', dodawanie(liczba1,liczba2))
