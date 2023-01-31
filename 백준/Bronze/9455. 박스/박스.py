for test_case in range(int(input())):
    m, n = map(int, input().split())
    box_list = [list(map(int, input().split())) for _ in range(m)]
    answer = 0
    for col in range(n):
        c_1 = 0
        for row in range(m):
            if box_list[m-row-1][col] == 1:
                answer += row-c_1
                c_1 += 1
    print(answer)