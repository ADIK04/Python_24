a,b,c = 456, 89, 1
print('Wartość a: ',a )
print('Wartość b: ',b )
print('Wartość c: ',c )

def NWD(a,b):
    if a > b:
        a, b = b, a
    for d in range(a, 0,-1):
        if a % d == 0  and b % d == 0:
            return d
a = int(input('Podaj a :'))
b = int(input('Podaj b :'))

print("NWD(" +  str(a) + str(b) + ")=", NWD(a, b))

