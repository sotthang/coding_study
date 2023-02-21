n, m = map(int, input().split())
li = [x for x in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    li[i-1:j-1+1] = li[i-1:j-1+1][::-1]
print(*li)