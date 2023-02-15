T = 10
for test_case in range(1, T + 1):
    n = int(input())
    k = input().split('+')
    answer = 0
    for x in k:
        if len(x) == 1:
            answer += int(x)
        else:
            temp = 1
            for y in x:
                if y.isnumeric():
                    temp *= int(y)
            answer += temp
    print(f'#{test_case} {answer}')