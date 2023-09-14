import sys

N = int(sys.stdin.readline())
rank = sorted([int(sys.stdin.readline()) for _ in range(N)])
ans = 0 
for x in range(N):
    if rank[x] != x+1:
        ans += abs(rank[x]-(x+1))
print(ans)