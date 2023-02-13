T = int(input())
for test_case in range(1, T + 1):
    a, b = 1, 1
    for x in input():
        if x == 'L':
            b += a
        else:
            a += b
    print(f'#{test_case} {a} {b}')