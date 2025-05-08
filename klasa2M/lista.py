#Lista to uporządkowana struktura danych, które może zawierać
# różne typy danych
lista = [] # pusta lista
lista_elementow = ['pies', 123,3.1415, -4, 'napis', True, False]
# Indeks 
print('Pierwszy element: ', lista_elementow[0])
print('Czwarty element: ', lista_elementow[3])
print('Od 3 elementu do końca: ', lista_elementow[2:])
print('Od początku  do 3 elementu: ', lista_elementow[:3])
print('Ostatni element listy: ', lista_elementow[-1])
# Stwórzcie listy owoców i warzyw. W liście owoców ma być 8 owoców w 
# liście warzyw 7 warzyw. Typ danych to napis(string)
warzywa = ['kalarepa','pomidor']
# 1.Wypisz piąty element z listy 
# 2. Wypiszcie elementy  od  drugiego elementu do końca listy warzywa
# 3. Wypiszcie elementy  od  początku  do 4 elementu z listy owoce
# 4. Wypiszcie zakres od 2 do 5  elementu z listy warzywa
# 5.Połączcie te dwie listy za pomocą +. Nazwijcie nową listę owoce_i_warzywa
# 6. Dodaj nowy owoc do listy owoce_i_warzywa za pomocą metody append '
warzywa.append('sałata')
print(warzywa)
# 7. Usun z listy owoce_i_warzywa 10 element za pomocą metody pop
# 8. Dodaj listę owoce_i_warzywa do listy owoce za pomocą metody append
# 9. Posortuj listę owoce_i_warzywa za pomocą metody sort
# lista_elementow.sort()


