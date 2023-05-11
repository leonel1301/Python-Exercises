def mult(a, b, n):
    if (a < 10) or (b < 10):
        return a * b
    else:
        ai = a // 10 ** (n // 2)
        ad = a - (ai * (10 ** (n // 2)))
        bi = b // 10 ** (n // 2)
        bd = b - (bi * (10 ** (n // 2)))
        z1 = mult(ai, bi, n / 2) * (10 ** n)
        z2 = (mult(ai, bd, n / 2) + mult(ad, bi, n // 2)) * (10 ** (n // 2))
        z3 = mult(ad, bd, n / 2)

        return z1 + z2 + z3


print(mult(98765678, 24680135, 8))es:", maximo)