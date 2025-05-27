####################KALKULATOR#####################
#////////////////////////funkcje////////////////////
def dodawanie(a,b):
    return a+b

#///////////////menu/////////////////////
print('Jakie działanie: ')
print('1.Dodawanie')

#////////////////logika//////////////////////////
wybor = input('Podaj swoj wybor: ')# tylko jeden raz

if wybor == '1':
    liczba1 = float(input('Podaj pierwsza liczbe: '))
    liczba2 = float(input('Podaj druga liczbe: '))
    if wybor == '1':
        print(liczba1, '+', liczba2, '=', dodawanie(liczba1,liczba2))

