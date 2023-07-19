n, m = map(int, input().split())
li = [list(input()) for _ in range(n)]
ans_x, ans_y = 0, 0
for x in li:
    if "X" not in x:
        ans_x += 1
for y in list(map(list, zip(*li))):
    if "X" not in y:
        ans_y += 1
print(max(ans_x, ans_y))