maks = 0

print('Podaj kolejne długości skoków: ')
a = float(input())

while a != 0:
    if a > maks:
        maks = a
    a = float(input())
print('\nNajdluzszy skok:',maks, 'm')