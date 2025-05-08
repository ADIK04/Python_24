najdluzszy = 0

print('Podaj kolejne dlugosci skokow: ')
a = float(input())

while a != 0:
    if a > najdluzszy:
        najdluzszy = a
    a = float(input())
print('\nNajdluzszy skok: ',najdluzszy, 'm')