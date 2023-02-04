T = int(input())
for test_case in range(1, T + 1):
    sudoku_list = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    for x in range(9):
        if len(set(sudoku_list[x])) != 9:
            answer = 0
            break
    transpose_sudoku_list = list(zip(*sudoku_list))
    if answer == 1:
        for y in range(9):
            if len(set(transpose_sudoku_list[y])) != 9:
                answer = 0
                break
    if answer == 1:
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                li = set([sudoku_list[x][y], sudoku_list[x+1][y], sudoku_list[x+2][y], sudoku_list[x][y+1], sudoku_list[x+1][y+1],
                sudoku_list[x+2][y+1], sudoku_list[x][y+2], sudoku_list[x+1][y+2], sudoku_list[x+2][y+2]])
                if len(li) != 9:
                    answer = 0
                    break
    print(f'#{test_case} {answer}')