print('----------------------------------------')
data_from_user = int(input('Podaj jakas liczbe: '))
print(data_from_user + 2)
# Algorytm przeliczajacy stopnie Fahrenheita na Celsjusze
print('----------------------------------------')
F = int(input('Stopnie w Fahrenheitach: '))
print(F, ' stopni Fahrenheita to ',(F - 32) * 5/9,'stopni Celcjusza.')
# Napisz algorytm przeliczajacy stopnie Celsjusza na stopnie Fahrenheita 
print('----------------------------------------')
C = int(input('Stopnie w Celcjuszach: '))
print(C, ' stopni Celcjusza to ',9/5 * C + 32,'stopni Fahrenheita.')

# Napisz algorytm przeliczajacy kilometry na mile oraz mile na kilometry
km  = float(input('Podaj kilometry: '))
print(km, ' kilometrów ',km * 0.625,'mil.')

mil  = float(input('Podaj mile: '))
print(mil, ' mil ',mil * 1.609,'kilometrów.')
