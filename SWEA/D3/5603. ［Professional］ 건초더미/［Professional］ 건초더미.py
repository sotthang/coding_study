T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = [int(input()) for _ in range(n)]
    answer = 0
    for x in li:
        answer += abs(x - (sum(li)//n))
    print(f'#{test_case} {answer//2}')