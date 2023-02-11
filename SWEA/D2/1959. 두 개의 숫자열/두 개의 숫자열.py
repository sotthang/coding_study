T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    answer = 0
    for x in range(max(a, b)-min(a, b)+1):
        temp = 0
        for y in range(min(a, b)):
            if a > b:
                temp += a_list[x+y] * b_list[y]
            else:
                temp += a_list[y] * b_list[x+y]
        if answer < temp:
            answer = temp
    print(f'#{test_case} {answer}')