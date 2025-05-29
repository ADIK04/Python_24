# ////////////////////////////KALKULATOR////////////////////////////
#////////////////////////////I. funkcje///////////////////////////////
def dodawanie(a,b):
    return a + b
# Dodaj kolejne funkcje(odejmowanie,mnozenie, dzielenie,resztazdzielenia,
#potegowanie,pierwiastkowanie)
#////////////////////////////II. menu///////////////////////////////
print('Wybierz działanie: ')
print('1.Dodawanie')
#dodaj kolejne działania do menu
#////////////////////////////III. logika///////////////////////////////
wybor = input('Podaj swoj wybor: ')

if wybor == '1':
    liczba1 = int(input('Podaj pierwsza liczbe: '))
    liczba2 = int(input('Podaj druga liczbe: '))
    if wybor == '1':
        print(liczba1, '+', liczba2, '=', dodawanie(liczba1,liczba2))
# w tej czesci dodaj kolejne 
