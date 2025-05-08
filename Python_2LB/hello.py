# 1.Wielkość liter ma znaczenie
a = 5 # zmienna o nazwie a
A = 5 # zmienna o nazwie A
# 2.Między wartościami a operatorami można wstawiać spacje
B = a + A # zmienna B jest sumą a i A
# 3.Kolejne instrukcje umieszczamy  w wierszach poniżej
# 4. Piszemy od początku wiersza
# 5.Tekst po znaku # jest komentarzem
# 6.O typie zmiennej decyduje nadana jej wartość
a = 5 # typ liczbowy zmiennej, dokładniej liczba całkowita
tekst = "hello world" # typ tekstowy zmiennej
# 7.Funkcja print() pozwala wyswietlić tekst w konsoli
print(a)
print(A)
print(B)
print(tekst)

# ----------------------------------------------------------------
print('*** Program powitalny ***')
login = input('Podaj nazwę użytkownika: ') #input jest to funkcja, która
# pobiera dane od użytkownika

print('----------------------------------')
print('Użytkownik <' + login + '> jest programistą Pythona')
print('----------------------------------')