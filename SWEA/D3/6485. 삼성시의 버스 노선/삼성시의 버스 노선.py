T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    bus_stop = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for x in range(a, b+1):
            bus_stop[x] += 1
    p = int(input())
    print(f'#{test_case}', end=' ')
    for _ in range(p):
        print(bus_stop[int(input())], end=' ')
    print()