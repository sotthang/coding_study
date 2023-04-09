T = int(input())
for test_case in range(1, T + 1):
    li = []
    s = input()
    S, D, H, C = 13, 13, 13, 13
    for x in range(len(s)//3):
        li.append(s[3*x:3*x+3])
    if len(set(li)) != len(s)//3:
        print(f'#{test_case} ERROR')
    else:
        for y in li:
            if y[0] == 'S':
                S -= 1
            elif y[0] == 'D':
                D -= 1
            elif y[0] == 'H':
                H -= 1
            elif y[0] == 'C':
                C -= 1
        print(f'#{test_case} {S} {D} {H} {C}')