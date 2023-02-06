T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = 0
    farm = [list(map(int, input())) for _ in range(n)]
    start, end = n//2, n//2+1
    for x in range(n):
        for y in range(start, end):
            answer += farm[x][y]
        if x < n//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{test_case} {answer}')