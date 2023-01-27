white_page = [[0 for _ in range(100)]for _ in range(100)]
for _ in range(int(input())):
    x_coordinate, y_coordinate = map(int, input().split())
    for x in range(x_coordinate, x_coordinate+10):
        for y in range(y_coordinate, y_coordinate+10):
            white_page[x][y] = 1
answer = 0
for c in white_page:
    answer += c.count(1)
print(answer)