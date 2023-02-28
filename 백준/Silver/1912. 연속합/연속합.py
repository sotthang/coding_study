n = int(input())
n_li = list(map(int, input().split()))
for x in range(1, n):
    n_li[x] = max(n_li[x], n_li[x-1]+n_li[x])
print(max(n_li))