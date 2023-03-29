T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    answer = 0
    for x in range(n-2):
        if li[x] < li[x+1] < li[x+2] or li[x] > li[x+1] > li[x+2]:
            answer += 1
    print(f'#{test_case} {answer}')