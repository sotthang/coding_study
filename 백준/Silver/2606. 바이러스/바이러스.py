pc = int(input())
line = int(input())
graph = [[] for _ in range(pc+1)]
start = 1
stack = [start]
visited = [False] * (pc+1)
visited[start] = True
for _ in range(line):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)
while stack:
    cur = stack.pop()
    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)
print(visited.count(True)-1)