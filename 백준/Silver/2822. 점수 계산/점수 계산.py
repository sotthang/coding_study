point = 0
n = []
for x in sorted([[i, int(input())] for i in range(1, 9)], key=lambda x: x[1], reverse=True)[:5]:
    n.append(x[0])
    point += x[1]
print(point)
print(*sorted(n[:5]))