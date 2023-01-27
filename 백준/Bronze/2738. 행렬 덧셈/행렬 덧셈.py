n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for a, b in zip(a, b):
    print(*[x+y for x, y in zip(a, b)])