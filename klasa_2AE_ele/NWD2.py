def NWD(a,b):
    while a !=b:
        if a > b:
            a = a - b # a -= b
        else:
            b = b - a # b -= a 
    return a 
a = int(input('Podaj liczbę a: '))
b = int(input('Podaj liczbę b: '))

print("NWD(" + str(a) + "," + str(b) + ")=", NWD(a,b))
