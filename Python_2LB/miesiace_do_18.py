# Napisz algorytm, ktory wyliczy ile zostalo miesiecy do 18 
print('Ktory mamy rok: ')
rok = int(input())
print('Podaj miesiac: ')
miesiac = int(input())
print('Podaj rok w ktorym sie urodziles: ')
rok_ur = int(input())

if rok - 18 > rok_ur:
    print('Masz juz 18 lat')
else:
    print('W jakim miesiacu sie urodziles: ')
    miesiac_ur = int(input())
    if rok_ur + 18 == rok and miesiac >= miesiac_ur:
        print('Jestes pelnoletni')
    else:
        print('Za ', (18 - (rok - rok_ur)) * 12 + miesiac_ur - miesiac,'miesiecy osiagniesz osiemnache')

