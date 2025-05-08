from colorama import Fore, Style
import random

wysokosc = 10

kolory_bombek = [Fore.RED,Fore.BLUE, Fore.YELLOW, Fore.MAGENTA]
#Tworzenie choinki
for wiersz in range(wysokosc):
    spacje = ' ' * (wysokosc-wiersz-1)
    linia = ''
    # for i in range(2 * wiersz + 1):
    #     if random.random() < 0.3:
    #         linia += random.choice(kolory_bombek) + 'O' + Style.RESET_ALL
    #     else:
    #         linia += Fore.GREEN + "*" + Style.RESET_ALL
    print(spacje + linia)
# Wyświetlenie świątecznych życzeń
zyczenia = "\n🎄 Wesołych Świąt i Szczęśliwego Nowego Roku! 🎅"
print(zyczenia)