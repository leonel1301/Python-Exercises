n = int(input())
while n:
    chars = str(input())
    n -= 1
    if len(chars) > 10:
        print(chars[0] + str(len(chars) - 2) + chars[len(chars) - 1])
    else:
        print(str(chars))
