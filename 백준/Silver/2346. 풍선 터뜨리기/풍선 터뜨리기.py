from collections import deque

n = int(input())
deq = deque(enumerate(map(int, input().split()), start=1))
for _ in range(n):
    p = deq.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        deq.rotate(-(p[1]-1))
    else:
        deq.rotate(-p[1])