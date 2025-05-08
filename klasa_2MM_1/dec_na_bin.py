# Cyfry wspak
lista = [0,0,0,0,0,0,0,0]
for i in range(8):
    lista[i] = int(input())
print(lista)
for cyfra in reversed(lista):
    print(cyfra, end=' ')
#Zamiana liczby dziesiętnej na binarną
cyfry = [0,0,0,0,0,0,0,0]
liczba = int(input('Podaj liczbę: '))
cyfry[7]= liczba % 2
iloraz = liczba // 2

i = 1 
while iloraz > 0:
    cyfry[7-i] = iloraz % 2
    iloraz //= 2
    i += 1

