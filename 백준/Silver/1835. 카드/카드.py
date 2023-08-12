from collections import deque

n = int(input())
card = deque()
card.append(n)

for x in range(n - 1, 0, -1):
    card.appendleft(x)
    for _ in range(x):
        card.appendleft(card.pop())

print(*card)
