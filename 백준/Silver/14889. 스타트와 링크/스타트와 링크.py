import sys

N = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 1e9
visited = [0] * (N + 1)

def dfs(depth, idx):
    global result
    if depth == (N // 2):
        start, link = 0, 0
        for i in range(N): 
            for j in range(i + 1, N):
                if visited[i] and visited[j]:
                    start += (array[i][j] + array[j][i])
                elif not visited[i] and not visited[j]:
                    link += (array[i][j] + array[j][i])
        
        result = min(result, abs(start - link))
    for i in range(idx, N): 
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0

dfs(0, 0)
print(result)