#Lista to jest zbiór, który może przechowywać wiele wartości

lista = [] # to jest pusta lista
lista_elementow= [123,3.1415, 'napis','kiełbasa',True, False]
print(lista_elementow)
print('Pierwszy element na liście: ',lista_elementow[0]) #indeks pierwszego elementu
print('Drugi element na liście: ',lista_elementow[1]) #indeks drugiego elementu
print('Ostatni element na liście: ',lista_elementow[-1]) #indeks ostatniego elementu
print('Od 3 elementu na liście: ',lista_elementow[2:]) #wypisuje od 3 elementu do końca
print('Ostatni element na liście: ',lista_elementow[2:]) #wypisuje od 3 elementu do końca
#Metody
#metoda append dodaje element jako ostatni na liście
print(lista_elementow.append(15))
print(lista_elementow)
lista_elementow.pop(0)
print(lista_elementow)
# Stwórzcie listy owoców i warzyw. W liście owoców ma być 8 owoców w 
# liście warzyw 7 warzyw
# Typ danych to napis(string)
# 1.Wypisz piąty element z listy 
# 2. Wypiszcie elementy  od  drugiego elementu do końca listy warzywa
# 3. Wypiszcie elementy  od  początku  do 4 elementu z listy owoce
# 4. Wypiszcie zakres od 2 do 5  elementu z listy warzywa
# 5.Połączcie te dwie listy. Nazwijcie nową listę owoce_i_warzywa
# 6. Dodaj nowy owoc do listy owoce_i_warzywa za pomocą metody append '
# 7. Usun z listy owoce_i_warzywa 10 element za pomocą metody pop
# 8. Dodaj listę owoce_i_warzywa do listy owoce 
# 9. Posortuj listę owoce_i_warzywa za pomocą metody sort
lista_elementow.sort()
