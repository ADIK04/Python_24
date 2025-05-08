#Lista to uporządkowana struktura danych, ktora moze zawierac 
# rozne typy danych
lista = [] # to jest pusta lista
lista_elementow = [123,3.1415,'string','niebo',True, False]
spozywka =['ser','mleko','bułka','jogurt','kefir','chleb','woda','sok','wafelek']
owoce = ['mango','arbuz','borowka','malina', 'winogrono','truskawka','jablko','gruszka','pomarańcza']
# INDEKS
print('Pierwszy element: ',spozywka[0])
print('Czwarty element: ',spozywka[3])
print('Ostatni element: ',spozywka[-1])
print('Od 2  elementu do końca: ',spozywka[1:])
print('Od poczatku  do 3 elemnetu: ',spozywka[:3])
#Łączenie list
spozywka_i_owoce = spozywka + owoce
print('Połączone listy: ',spozywka_i_owoce)
# 1.Wypisz przedostatni element z listy spozywka_i_owoce
# 2. Wypiszcie elementy  od  5 elementu do końca listy spozywka_i_owoce
# 3. Wypiszcie elementy  od  początku  do 5 elementu z listy spozywka_i_owoce
# 4. Wypiszcie zakres od 3 do 8  elementu z listy spozywka_i_owoce
# 5. Dodaj nowy owoc do listy spozywka_i_owoce za pomocą metody append '
# 6. Usun z listy spozywka_i_owoce 10 element za pomocą metody pop
# 7. Posortuj listę spozywka_i_owoce za pomocą metody sort
