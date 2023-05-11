def doubleSum(num):
    if num == 0:
        return 0
    else:
        return 2 * num + doubleSum(num - 1)


n = int(input("Ingrese el numero: "))
result = doubleSum(n)
print(result)
