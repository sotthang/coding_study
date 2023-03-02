T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    d = 0
    if a == b == c:
        d = a
    elif a == b:
        d = c
    elif b == c:
        d = a
    else:
        d = b
    print(f'#{test_case} {d}')