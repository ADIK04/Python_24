from rich.console import Console
import random

def choinka():
    console = Console()
    wysokosc = int(input("Podaj wysokość choinki: "))
    kolory_bombek = ["red", "blue", "yellow", "orange"]
    for wiersz in range(wysokosc):
        spacje = ' ' * (wysokosc - wiersz - 1)
        linia = ''
        for i in range(2 * wiersz + 1):
            if random.random() < 0.3:
                kolor = random.choice(kolory_bombek)
                linia += f"[{kolor}]o[/]"
            else:
                linia += "[green]*[/]"
        console.print(spacje + linia)

choinka()

# Życzenia Świąteczne
zyczenia = "\n🎄 [bold green]Wesołych Świąt[/] i [bold red]Szczęśliwego Nowego Roku! 🎅[/]"
console = Console()
console.print(zyczenia)
