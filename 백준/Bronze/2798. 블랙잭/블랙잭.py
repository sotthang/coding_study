n, m = map(int, input().split())
card_list = list(map(int, input().split()))
answer = 0
for x in range(n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            card = card_list[x]+card_list[y]+card_list[z]
            if m-answer >= m-card and card <= m:
                answer = card
print(answer)