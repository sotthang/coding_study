T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    n = int(input())
    c = 0
    li = []
    while n != c:
        c += 1
        if c == 1:
            li.append([1])
        elif c == 2:
            li.append([1, 1])
        else:
            lili = [1]
            for x in range(c-2):
                lili.append(li[c-2][x]+li[c-2][x+1])
            lili.append(1)
            li.append(lili)
        print(*li[c-1])