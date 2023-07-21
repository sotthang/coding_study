n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
same_class = [[0] * n for _ in range(n)]

for x in range(5):
    for y in range(n):
        for z in range(y + 1, n):
            if li[y][x] == li[z][x]:
                same_class[z][y], same_class[y][z] = 1, 1

c = [s.count(1) for s in same_class]

print(c.index(max(c)) + 1)