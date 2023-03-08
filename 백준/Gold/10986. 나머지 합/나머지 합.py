import sys

N,M= map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sum = 0
numdp = [0] * M
for i in range(N):
    sum += num[i]
    numdp[sum % M] += 1
answer = numdp[0]
for i in numdp:
    answer += i*(i-1)//2
print(answer)