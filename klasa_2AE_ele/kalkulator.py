#########KALKULATOR#####################
#/////////////funkcje//////////////////
def dodawanie(a,b):
    return a+b

#/////////////menu///////////////////
print('Podaj działanie: ')
print('1.Dodawanie')


#////////////wybor/////////////////
wybor = input('Jakie działanie: ') # tylko jeden raz

if wybor == ('1'):
    liczba1 = float(input('Podaj pierwszą liczbę: '))
    liczba2 = float(input('Podaj drugą liczbę: '))
    if wybor == '1':
        print(liczba1, '+', liczba2,'=', dodawanie(liczba1,liczba2))
