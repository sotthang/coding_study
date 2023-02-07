import math
for _ in range(int(input())):
    answer = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(int(input())):
        cx, cy, r = map(int, input().split())
        d1 = math.sqrt(((x1-cx)**2) + ((y1-cy)**2))
        d2 = math.sqrt(((x2-cx)**2) + ((y2-cy)**2))
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            answer += 1
    print(answer)