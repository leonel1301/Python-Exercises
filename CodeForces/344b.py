def f(a,b,c):
    for x in range(a + 1):
        y = b - x
        z = (a - x)
        if z < 0 or y < 0:
            break;
        if x + z == a and x + y == b and y + z == c:
            print(x, y, z)
            return
    print("Impossible")

a, b, c = map(int, input().split())
f(a,b,c)
