data_from_user = (input('Podaj jakies dane: '))
print(data_from_user + '2')

# Algorytm przeliczajacy stopnie Fahrenheita na Celsjusze
F = int(input('Temperatura w st. Fahrenheita: '))
print(F, ' stopni Fahrenheita to ',(F - 32) * 5/9 , 'stopni Celsjusza.')

# Napisz algorytm przeliczajacy stopnie Celsjusza na Fahrenheita
C = float(input('Temperatura w st. Celcjusza: '))
print(C, ' stopni Celcjusza to ',9/5 * C + 32 , 'stopni Fahrenheita.')

# Napisz algorytm przeliczajacy kilometry na mile i odwrotnie
km = float(input('Podaj kilometry: '))
print(km, ' kilometrów to ',km * 0.625 , 'mil.')

m = float(input('Podaj mile: '))
print(m, ' mil to ',m * 1.609 , 'kilometrów.')
