import itertools

for x in itertools.combinations([int(input()) for _ in range(9)], 7):
    if sum(x) == 100:
        for y in x:
            print(y)
        break