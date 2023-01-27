import sys
n, m = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline().strip() for _ in range(n)])
c = 0
for _ in range(m):
    if input() in s:
        c += 1
print(c)