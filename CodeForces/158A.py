participents_count, position = map(int, input().split(' '))
scores = list(map(int, input().split()))

aprobate = 0
for values in scores:
    if values >= scores[position-1] and values > 0:
        aprobate += 1

print(aprobate)