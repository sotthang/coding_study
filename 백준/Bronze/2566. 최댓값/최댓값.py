max_num, row, col = 0, 0, 0
for r in range(1, 10):
    rows = list(map(int, input().split()))
    maximum = max(rows)
    if max_num <= maximum:
        max_num = maximum
        row = r
        col = rows.index(maximum)+1
print(max_num)
print(row, col)