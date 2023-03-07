import sys

n, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
answer = [sum(n_list[:k])]
for x in range(n-k):
    answer.append(answer[x] - n_list[x] + n_list[k+x])
print(max(answer))