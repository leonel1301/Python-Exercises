def criba_eratostenes(n):
    primos = []
    for i in range(n + 1):
        primos.append(i)
    for i in range(2, n + 1):

