def NWD_odejmowanie(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 
a = int(input('Podaj a :'))
b = int(input('Podaj b :'))

print("NWD(" +  str(a) + str(b) + ")=", NWD(a, b))