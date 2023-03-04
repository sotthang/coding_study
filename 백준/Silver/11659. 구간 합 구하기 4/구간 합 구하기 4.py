import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
for x in range(1, n):
    n_list[x] += n_list[x-1]
n_list.insert(0, 0)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(n_list[j] - n_list[i-1])
