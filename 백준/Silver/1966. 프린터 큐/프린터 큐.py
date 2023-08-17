from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = deque([(x, idx) for idx, x in enumerate(deque(map(int, input().split())))])
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())
