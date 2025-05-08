# Lista to uporządowana struktura danych, ktora moze zawierac 
# rozne typy danych
nietoperz = [] # pusta lista o nazwie nietoperz
lista_elementow=['statek', 123, -1, 3.1415, True, False, 'jabłko']

# Indeksowanie 
print('Pierwszy element listy: ', lista_elementow[0])
print('Piąty element listy: ', lista_elementow[4])
print('Od 2 elementu do końca: ', lista_elementow[1:])
print('Od początku listy do 3 elementu: ', lista_elementow[:3])
print('Ostatni element listy: ', lista_elementow[-1])
print('Liczba elemnetów listy: ',len(lista_elementow))

# Stwórzcie dwie osobne listy owoców i warzyw. W liście owoców ma być 8 owoców w 
# liście warzyw 7 warzyw. Typ danych to napis(string)
warzywa = ['kalarepa','pomidor']
# 1.Wypisz piąty element z listy owoce lub warzywa
# 2. Wypiszcie elementy  od  drugiego elementu do końca listy warzywa
# 3. Wypiszcie elementy  od  początku  do 4 elementu z listy owoce
# 4. Wypiszcie zakres od 2 do 5  elementu z listy warzywa
# 5.Połączcie te dwie listy za pomocą +. Nazwijcie nową listę owoce_i_warzywa
# 6. Dodaj nowy owoc do listy owoce_i_warzywa za pomocą metody append '
warzywa.append('sałata')
print(warzywa)
# 7. Usun z listy owoce_i_warzywa 10 element za pomocą metody pop(sprawdz na w3schools)
# 8. Dodaj listę owoce_i_warzywa do listy owoce za pomocą metody append
# 9. Posortuj listę owoce_i_warzywa za pomocą metody sort(sprawdz na w3schools)



