T = int(input())
for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    li = list(map(int, input().split()))
    answer = 200000
    for x in range(1 << n):
        total = 0
        for y in range(n):
            if x & (1 << y):
                total += li[y]
        if 0 <= (total - b) < answer:
            answer = total - b
    print(f'#{test_case} {answer}')