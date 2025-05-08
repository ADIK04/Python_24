maks_skok = 0
print('Podaj kolejne długości skoków: ')
skok = float(input())

while skok != 0:
    if skok > maks_skok:
        maks_skok = skok
    skok = float(input())

print('\nNajdłuższy skok: ', maks_skok, 'm')
