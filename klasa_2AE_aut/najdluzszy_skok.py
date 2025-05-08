najdluzszy_skok = 0

print('Podaj kolejne dlugosci skokow: ')
skok = float(input())

while skok != 0:
    if skok > najdluzszy_skok:
        najdluzszy_skok = skok
    skok = float(input())
print('\nNajdluzszy skok: ', najdluzszy_skok, 'm')
    