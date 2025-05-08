wysokosc = int(input('Podaj wysokosc choinki: '))

for wiersz in range(wysokosc):
    spacje = ' '  * (wysokosc-wiersz-1)
    gwiazdki = '*' * (2 * wiersz +1)
    print(spacje + gwiazdki)

#Pień choinki
pien = ' ' * (wysokosc - 1) + '|'
print(pien)
print(pien)

zyczenia = '\n🎄 Wesolych Świąt i Szczęśliwego Nowego Roku🧑‍🎄'
print(zyczenia)