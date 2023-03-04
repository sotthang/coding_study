import sys
from collections import deque

deq = deque([])
for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().rstrip()
    if 'push' in n:
        deq.append(n.split()[1])
    elif n == 'pop':
        print(deq.popleft()) if deq else print(-1)
    elif n == 'size':
        print(len(deq))
    elif n == 'empty':
        print(0) if deq else print(1)
    elif n == 'front':
        print(deq[0])if deq else print(-1)
    else:
        print(deq[-1])if deq else print(-1)