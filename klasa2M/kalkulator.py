#--------------------KALKULATOR--------------------
# ...................I.funkcje.....................
def dodawanie(a,b):
    return a + b
def odejmowanie(a,b):
    return a - b
# ...................II.Menu.......................
print('Podaj działanie do obliczenia: ')
print('1.Dodawanie') 
# Uzupełnij menu kolejnymi działaniami
# ...................III.Wyliczanie.....................
wybor = input('Podaj działanie: ')

if wybor == '1':
    liczba1 = int(input('Podaj pierwszą liczbę: '))
    liczba2 = int(input('Podaj drugą liczbę: '))
    if wybor == '1':
        print(liczba1, '+', liczba2, '=', dodawanie(liczba1,liczba2))
