ball_list = [1, 2, 3]
for _ in range(int(input())):
    x, y = map(int, input().split())
    x_change, y_change = ball_list.index(x), ball_list.index(y)
    ball_list[x_change], ball_list[y_change] = ball_list[y_change], ball_list[x_change]
print(ball_list[0])