year = int(input())


def all_distinct(num: int) -> bool:
    s = set()
    while num > 0:
        last_digit = num % 10
        if last_digit in s:
            return False
        s.add(last_digit)
        num //= 10
    return True


aux = year + 1
while not all_distinct(aux):
    aux += 1
print(aux)
