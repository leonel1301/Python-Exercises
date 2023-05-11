number_a, number_b = map(int, input().split())


def all_distinct(num_a: int) -> bool:
    s = set()
    while num_a > 0:
        last_digit = num_a % 10
        if last_digit in s:
            return False
        s.add(last_digit)
        num_a //= 10
    return True


if number_b != number_a:
    aux = number_a + 1
else:
    aux = number_a
while not all_distinct(aux):
    if aux >= number_b:
        print("-1")
        break
    aux += 1
if all_distinct(aux):
    print(aux)
