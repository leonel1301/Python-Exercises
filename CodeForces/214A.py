n, m = map(int, input().split())
count = 0
for a in range(0, int(n ** 0.5) + 1):
    if a + (n - a ** 2) ** 2 == m:
        count += 1
print(count)