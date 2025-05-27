# ///////////////KALKULATOR///////////////////////
# ..........................funkcje........................
def dodawanie(a,b):
    return a + b
# Uzupełnij kolejnymi funkcjami-odejmowanie,mnożenie,dzielenie,reszta z dzielenia
# ,potęgowanie,pierwiastkowanie
# ..........................menu..........................
print('Podaj działanie: ')
print('1.Dodawanie')
# uzupełnij menu kolejnymi działaniami
# ...........................logika..........................
wybor = (input('Podaj swoj wybor: '))

if wybor == '1':
    liczba1 = int(input('Podaj pierwszą liczbę: '))
    liczba2 = int(input('Podaj drugą  liczbę: '))
    if wybor == '1':
        print(liczba1, '+', liczba2, '=',dodawanie(liczba1,liczba2))
# uzupelnij logike dla kolejnych działąn


