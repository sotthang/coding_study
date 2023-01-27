import sys
import heapq

heap = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if not heap and num == 0:
        print(0)
    elif num != 0:
        heapq.heappush(heap, (abs(num), num))
    elif num == 0:
        print(heapq.heappop(heap)[1])