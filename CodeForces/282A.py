import sys;

n = int(input())
x = 0
while(n):
    n -= 1
    cod = list(input())
    if cod.count("+") == 2:
        x += 1
    if cod.count("-") == 2:
        x -= 1
print(x)
