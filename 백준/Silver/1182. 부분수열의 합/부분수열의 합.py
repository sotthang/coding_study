import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for x in range(1, n+1):
    comb = combinations(arr, x)
    for x in comb:
        if sum(x) == s:
            ans += 1
print(ans)