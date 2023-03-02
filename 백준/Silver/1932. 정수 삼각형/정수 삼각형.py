n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
for x in range(1, n):
    for y in range(x+1):
        if y == 0:
            tri[x][y] += tri[x-1][y]
        elif y == x:
            tri[x][y] += tri[x-1][y-1]
        else:
            tri[x][y] = max(tri[x][y]+tri[x-1][y-1], tri[x][y]+tri[x-1][y])

print(max(tri[-1]))
