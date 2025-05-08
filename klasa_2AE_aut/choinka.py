# Wysokość choinki
wysokosc = 10

# Rysowanie choinki za pomocą pętli for
for wiersz in range(wysokosc):
    spacje = " " * (wysokosc - wiersz - 1)
    gwiazdki = "*" * (2 * wiersz + 1)
    print(spacje + gwiazdki)

# Rysowanie pnia choinki
pień = " " * (wysokosc - 1) + "|"
print(pień)
print(pień)

# Wyświetlenie świątecznych życzeń
zyczenia = "\n🎄 Wesołych Świąt i Szczęśliwego Nowego Roku! 🎅"
print(zyczenia)
