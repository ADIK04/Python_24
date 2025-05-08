#Lista to uporządkowana struktura danych, ktora moze zawierac roznetypy danych
lista = [] # to jest pusta lista
lista_elementow= [123,3.1415, 'napis','kiełbasa',True, False]
warzywa = ['rzepa', 'ziemniak', 'papryka', 'cebula', 'marchewka', 'pomidor','']
owoce = ['mandarynka','jablko','morela', 'brzoskwinia', 'gruszka','banan','mango']
warzywa_i_owoce = warzywa + owoce # łączenie dwóch list ze sobą
print(warzywa_i_owoce)
# Indeks 
print('Pierwszy element: ', warzywa[0])
print('Trzeci element: ', warzywa[2])
print('Ostatni element',warzywa[-1])
print('Od 3 elementu do końca listy', warzywa_i_owoce[2:])
print(warzywa_i_owoce)
print('od poczatku listy do 4', warzywa_i_owoce[:4])
print('Zakres elelmentów od 2 do 4',warzywa_i_owoce[1:4])
#Metody
warzywa_i_owoce.append('kiwi')# dodawanie elementu na koniec listy
print(warzywa_i_owoce)
# 1.Wypisz przedostatni element z listy 
# 2. Wypiszcie elementy  od  5 elementu do końca listy warzywa_i_owoce
# 3. Wypiszcie elementy  od  początku  do 5 elementu z listy warzywa_i_owoce
# 4. Wypiszcie zakres od 3 do 8  elementu z listy warzywa_i_owoce
# 5. Dodaj nowy owoc do listy owoce_i_warzywa za pomocą metody append '
# 6. Usun z listy owoce_i_warzywa 10 element za pomocą metody pop
# 7. Posortuj listę owoce_i_warzywa za pomocą metody sort