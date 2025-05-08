lista = [12, 3.1453, 'napis', True, False]
print('Elementy listy to: ', lista)
print('Pierwszy element listy: ', lista[0])
print('Drugi element listy: ', lista[1])

owoce = ['banan','kiwi','gruszka', 'śliwka', 'jabłko', 'winogorn']
print(owoce[0:]) # wypisujemy całą listę od początku
print(owoce[2:]) # od 3 elementu do końca
print(owoce[2:4]) # element 3 i 4 z listy owoce
warzywa = ['ogórek','pomidor','dynia','burak','marchew','pietruszka']
owoce_i_warzywa = owoce + warzywa
print('Polaczone dwie listy: ', owoce_i_warzywa)
print('Wypisanie ostatniego elemntu z listy: ', owoce_i_warzywa[-1])
print('Sprawdza długość listy. Lista ma ', len(owoce_i_warzywa) , 'elementów.')

# Stwórzcie listy owoców i warzyw. W liście owoców ma być 8 owoców
#  w liście warzyw 7 warzyw

# 5.Połączcie te dwie listy. Nazwijcie nową listę owoce_i_warzywa
# 6. Dodaj nowy owoc do listy owoce_i_warzywa za pomocą metody append 
owoce_i_warzywa.append('kalafior')
print(owoce_i_warzywa)
# 7. Usun z listy owoce_i_warzywa 10 element za pomocą metody pop
owoce_i_warzywa.pop(0)#usuwanie pierwszwego elementu z listy
print(owoce_i_warzywa)
# 8. Dodaj listę owoce_i_warzywa do listy owoce za
# 9. Posortuj listę owoce_i_warzywa za pomocą metody sort
owoce_i_warzywa.sort()
print(owoce_i_warzywa)



