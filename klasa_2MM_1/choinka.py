# Wysokość choinki
wysokosc = int(input('Podaj wysokosc choinki: '))

for wiersz in range(wysokosc):
    spacja = ' ' * (wysokosc- wiersz - 1)
    gwiazdki = '*' * (2 * wiersz + 1)
    print(spacja + gwiazdki)

# Pień choinki
pien = ' ' * (wysokosc - 1) + '|'
print(pien)
print(pien)
# Zyczenia
zyczenia = '\n🎄Wesołych Świąt i Szczęsliwego Nowego Roku🧑‍🎄'
print(zyczenia)
