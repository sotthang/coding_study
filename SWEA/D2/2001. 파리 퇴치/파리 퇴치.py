T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for x in range(n-m+1):
        for y in range(n-m+1):
            temp = 0
            for a in range(m):
                for b in range(m):
                    temp += li[x+a][y+b]
            if answer < temp:
                answer = temp
    print(f'#{test_case} {answer}')