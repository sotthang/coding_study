import sys

n, m = map(int, sys.stdin.readline().split())
poke = {}
for i in range(1, n+1):
    a = sys.stdin.readline().rstrip()
    poke[i] = a
    poke[a] = i
for _ in range(m):
    q = sys.stdin.readline().rstrip()
    print(poke[int(q)]) if q.isdigit() else print(poke[q])