import sys
import itertools

n = int(sys.stdin.readline())
answer = dict(zip(sys.stdin.readline().split(), [i for i in range(n)]))
reply = sys.stdin.readline().split()
point = 0
for p in list(itertools.combinations(reply, 2)):
    if answer.get(p[0]) < answer.get(p[1]):
        point += 1
print("%d/%d" % (point, n*(n-1)/2))