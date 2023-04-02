T = int(input())

for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    print(f'#{test_case} {sum([x if x >= 40 else 40 for x in li])//len(li)}')