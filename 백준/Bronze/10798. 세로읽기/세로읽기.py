read_list = [[0]*15 for _ in range(5)]
max_len = 0
for row in range(5):
    n = input()
    n_len = len(n)
    if max_len < n_len:
        max_len = n_len
    for col in range(n_len):
        read_list[row][col] = n[col]
for x in range(max_len):
    for y in range(5):
        if read_list[y][x] == 0:
            continue
        else:
            print(read_list[y][x], end='')