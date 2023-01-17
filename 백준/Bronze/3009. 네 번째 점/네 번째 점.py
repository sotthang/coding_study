x = []
y = []
for p in range(3):
    a, b = list(map(int, input().split()))
    x.append(a) if a not in x else x.remove(a)
    y.append(b) if b not in y else y.remove(b)

print(x[0], y[0])