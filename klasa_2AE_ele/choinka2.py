from colorama import Fore

wysokosc = 10
for wiersz in range(wysokosc):
    spacje = " " * (wysokosc - wiersz - 1)
    gwiazdki = "*" * (2 * wiersz + 1)
    print(Fore.GREEN + spacje + gwiazdki + Fore.RESET)

print(Fore.RED + "🎄 Wesołych Świąt! 🎄" + Fore.RESET)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
from colorama import Fore, Style
import random

# Wysokość choinki
wysokosc = 10

# Lista kolorów bombek
kolory_bombek = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Tworzenie choinki
for wiersz in range(wysokosc):
    spacje = " " * (wysokosc - wiersz - 1)
    linia = ""
    for i in range(2 * wiersz + 1):
        if random.random() < 0.3:  # 30% szans na bombkę
            linia += random.choice(kolory_bombek) + "O" + Style.RESET_ALL
        else:
            linia += Fore.GREEN + "*" + Style.RESET_ALL
    print(spacje + linia)

# Rysowanie pnia
pień = " " * (wysokosc - 1) + Fore.YELLOW + "|" + Style.RESET_ALL
print(pień)
print(pień)

# Świąteczne życzenia
zyczenia = Fore.RED + "\n🎄 Wesołych Świąt i kolorowych prezentów! 🎁" + Style.RESET_ALL
print(zyczenia)
