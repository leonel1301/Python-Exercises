n = int(input())
prod = 0
for i in range(0, n):
    numbers = input().split()
    if numbers.count("1") >= 2:
        prod += 1
print(prod)