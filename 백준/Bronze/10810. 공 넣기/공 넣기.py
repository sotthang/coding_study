n, m = map(int, input().split())
li = [0]*n
for _ in range(m):
    a, b, c = map(int, input().split())
    li[a-1:b-1+1] = [c]*(b-a+1)
print(*li)