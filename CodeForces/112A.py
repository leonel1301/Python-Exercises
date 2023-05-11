s = str(input().lower())
t = str(input().lower())
num_1 = []
num_2 = []
for letra in range(len(s)):
    num_1.append(ord(s[letra]) - 96)
for letra in range(len(t)):
    num_2.append(ord(t[letra]) - 96)
num_1.sort()
num_2.sort()
entero1 = int(''.join([str(i) for i in num_1]))
entero2 = int(''.join([str(i) for i in num_2]))
if entero1 < entero2:
    print("-1")
elif entero1 > entero2:
    print("1")
else:print("0")
