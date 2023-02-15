T = 10
for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case}', sum(list(map(int, input().split('+')))))