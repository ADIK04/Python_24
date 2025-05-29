def czypierwsza(n):
    for i in range(2,n):
        if n % i == 0 :
            return 0
    return 1

for i in range(1001, 1000000000, 2):
    if czypierwsza(i):
        print(i, end=' ') 