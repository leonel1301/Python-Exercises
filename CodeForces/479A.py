a = int(input())
b = int(input())
c = int(input())

ans = 0
if a == 1:
    ans = a + b
    if c == 1:
        ans += c
    else:
        ans *= c
elif b == 1:
    ans = (b + min(a,c)) * max(a, c)
elif c == 1:
    ans = (b + c) * a
else:
    ans = a * b * c

print(ans)