def solution(m, n, puddles):
    roads = [[0]*(m+1) for _ in range(n+1)]
    roads[1][1] = 1
    for x, y in puddles:
        roads[y][x] = -1
    for a in range(1, n+1):
        for b in range(1, m+1):
            if roads[a][b] == -1:
                roads[a][b] = 0
                continue
            roads[a][b] += (roads[a - 1][b] + roads[a][b - 1]) % 1000000007
    return roads[n][m]