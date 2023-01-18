T = int(input())
for test_case in range(1, T+1):
    for x in input().split():
        print(x[::-1], end=' ')