T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    print(f'#{test_case} {list(map(lambda x:x<=sum(li)//n, li)).count(True)}')