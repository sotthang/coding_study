rect_list = [[0] * 100 for _ in range(100)]
answer = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            rect_list[y][x] = 1
for s in rect_list:
    answer += s.count(1)
print(answer)