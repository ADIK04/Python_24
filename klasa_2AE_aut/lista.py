#Lista to uporządkowana struktura danych, 
# ktora moze zawierac rozne typy danych
lista = [] # to jest pusta lista
lista_elementow = [123,3.14158,'string','tekst',True,False]
jezyki_programowania1 = ['Fortran', 'C','Algol', 'BASIC']
jezyki_programowania2 = ['C++','Ruby', 'Java','JavaScript','C#','Node.js','React',\
                         'Angular','Go']
jezyki_programowania = jezyki_programowania1 + jezyki_programowania2 # laczenie list
print('Jezyki programowania: ',jezyki_programowania)
#Indeks 
print('Pierwszy element: ', jezyki_programowania2[0])
print('Piaty element: ', jezyki_programowania2[4])
print('Od 2 elementu do końca: ', jezyki_programowania2[1:])
print('Od poczatku  do 4 elementu: ', jezyki_programowania[:4])
print('Ostatni element: ', jezyki_programowania[-1])
print('Zakres elementów od 2 do 4: ', jezyki_programowania[1:4])
#Metody
jezyki_programowania.append('Python')
print('Lista po dodaniu Pythona',jezyki_programowania)

# 1.Wypisz przedostatni element z listy jezyki_programowania
# 1
# 2. Wypiszcie elementy  od  5 elementu do końca listy jezyki_programowania
# 3. Wypiszcie elementy  od  początku  do 5 elementu z listy jezyki_programowania
# 4. Wypiszcie zakres od 3 do 8  elementu z listy jezyki_programowania
# 5. Dodaj nowy język  do listy jezyki_programowania za pomocą metody append 
# 6. Usun z listy jezyki_programowania 10 element za pomocą metody pop
# 7. Posortuj listę jezyki_programowania za pomocą metody sort
