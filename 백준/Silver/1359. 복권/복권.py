from itertools import combinations

n, m, k = map(int,input().split())
ans = 0
case = [*combinations([i for i in range(n)], m)]

for x in case:
  c = 0
  for y in range(m):
    if x[y] < m:
      c += 1
  if c >= k:
    ans += 1

print(ans / len(case))