import sys
n = int(sys.stdin.readline())
stick = [int(sys.stdin.readline()) for _ in range(n)]
answer, max = 0, 0
for x in range(n-1, -1, -1):
    if stick[x] > max:
        answer += 1
        max = stick[x]
print(answer)