# 1.Wielkośc liter w kodzie ma znaczenie
a = 5
A = 10
# 2. Między wartościami, a operatorami(+,-,*,/,//,%,**) wstawiamy spacje
suma = a + A
# 3. Kolejne instrukcje umieszczamy w kolejnych wierszach
# 4.Tekst po znaku # jest komentarzem
# 5. O typie zmiennej decyduje nadana jej wartość
tekst = 'hello' # zmienna z wartością tekstową
# 6.Kod piszemy od początku linijki
# 7. Funkcja print() pozwala wyswietlic kod na ekranie
print(suma)
print(tekst)

# ----------------------------------------------------------------------------------
print('*** Progrma powitalny ***')
login  = input('Podaj nazwę użytkownika: ') 
# input to funkcja która pobiera dane od użytkownika 
print('-----------------------------------------')
print('Użytkownik <' + login + '> został programistą Pythona')
print('-----------------------------------------')