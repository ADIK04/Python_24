#Jednolinjkowe przypisywanie wartości do zmiennych
# a ,b, c = 12, 45, 89

# print('To jest a:',a)
# print('To jest b:',b)
# print('To jest c:',c)

def NWD(a,b):
    if a > b:
        a, b = b, a
    for d in range(a, 0, -1):
        if a % d == 0 and b % d == 0:
            return d
a = int(input('Podaj liczbę a: '))
b = int(input('Podaj liczbę b: '))

print("NWD(" + str(a) + "," + str(b) + ")=", NWD(a,b))
        



