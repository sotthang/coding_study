import sys
import heapq

heap = []
rubber_duck = sys.stdin.readline().strip()
while rubber_duck != '고무오리 디버깅 끝':
    rubber_duck = sys.stdin.readline().strip()
    if rubber_duck =='문제':
        heapq.heappush(heap, '문제')
    elif rubber_duck == '고무오리' and not heap:
        heapq.heappush(heap, '문제')
        heapq.heappush(heap, '문제')
    elif rubber_duck == '고무오리':
        heapq.heappop(heap)
print('힝구') if heap else print('고무오리야 사랑해')