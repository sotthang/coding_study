body_list = [tuple(map(int, input().split())) for t in range(int(input()))]
answer = []
for x in body_list:
    c = 1
    for y in body_list:
        if x == y:
            continue
        elif x[0] < y[0] and x[1] < y[1]:
            c += 1
    answer.append(c)
print(*answer)