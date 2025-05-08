print('Podaj obecny rok: ')
rok = int(input())
print('Podaj obecny miesiac: ')
miesiac = int(input())
print('W ktorym roku sie urodziles: ')
rok_ur = int(input())

if rok - 18 > rok_ur:
    print('Jesteś już pełnoletni')
else:
    print('W jakim miesiacu sie urodziles: ')
    miesiac_ur = int(input())
    if rok_ur + 18 == rok and miesiac >= miesiac_ur:
        print('Jestes juz pelnoletni')
    else:
        print('Za',(18 - (rok - rok_ur)) * 12 + miesiac_ur - miesiac,\
              'miesiecy osiagniesz osiemnache.')