for test_case in range(1, 11):
    t = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    transpose_li = list(zip(*li))
    answer, temp, re_temp = 0, 0, 0
    for x in range(100):
        if answer < sum(li[x]):
            answer = sum(li[x])
        if answer < sum(transpose_li[x]):
            answer = sum(transpose_li[x])
        temp += li[x][x]
        re_temp += li[x][99-x]
    print(f'#{test_case} {max(answer, temp, re_temp)}')