import sys

n = int(sys.stdin.readline())
answer = 0
for x in range(1, n+1):
    if x ** 2 <= n:
        answer += 1
    else:
        break
print(answer)