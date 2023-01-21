T = int(input())
for test_case in range(1, T + 1):
    line_index = [0, 0, 0, 0, 0, 0, 0, 0]
    answer = 'yes'
    for x in range(8):
        line = list(input())
        if line.count('O') != 1:
            answer = 'no'
        elif line_index[line.index('O')] == 0:
            line_index[line.index('O')] = 1
        elif line_index[line.index('O')] == 1:
            answer = 'no'
    print(f'#{test_case} {answer}')
