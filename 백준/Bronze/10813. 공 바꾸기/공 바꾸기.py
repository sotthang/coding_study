n, m = map(int, input().split())
li = [x for x in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    li[a-1], li[b-1] = li[b-1], li[a-1]
print(*li)