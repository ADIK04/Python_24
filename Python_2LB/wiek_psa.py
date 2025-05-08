wiek_psa = int(input('Podaj wiek psa: '))
if wiek_psa == 1:
    wiek_psa = 16
    print(' Wiek psa to :', wiek_psa, 'lat')
elif wiek_psa == 2:
    wiek_psa = 24
    print(' Wiek psa to :', wiek_psa, 'lat')
else:
    wiek_psa = 14 + (wiek_psa * 5)
    print(' Wiek psa to :', wiek_psa, 'lat')

