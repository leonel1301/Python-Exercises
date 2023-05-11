n = int(input())


def isLucky(n) -> bool:
    s = str(n)
    digits = set(s)
    if len(digits) == 1 and ('7' in digits or '4' in digits):
        return True
    elif len(digits) == 2 and ('7' in digits and '4' in digits):
        return True
    return False


flag = False
for i in range(4, min(477 + 1, n + 1)):
    if n % i == 0 and isLucky(i):
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")
