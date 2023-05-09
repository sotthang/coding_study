import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = 1e9
graph = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for i in graph:
    for j in i:
        print(0, end=' ') if j == inf else print(j, end=' ')
    print()