import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max = max(score)

for x, y in enumerate(score):
    score[x] = y / max * 100

print(sum(score)/n)