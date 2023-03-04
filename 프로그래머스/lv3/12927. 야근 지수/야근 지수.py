import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    else:
        heap = []
        for x in works:
            heapq.heappush(heap, [-x, x])
        while n > 0:
            temp = heapq.heappop(heap)
            heapq.heappush(heap, [temp[0]+1, temp[1]-1])
            n -= 1
        for x in heap:
            answer += x[1]**2
        return answer