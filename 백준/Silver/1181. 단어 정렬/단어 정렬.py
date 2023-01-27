import sys
import heapq

heap = []
for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().strip()
    if (len(word), word) not in heap:
        heapq.heappush(heap, (len(word), word))
for _ in range(len(heap)):
    print(heapq.heappop(heap)[1])