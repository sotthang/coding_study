def solution(board, moves):
    answer = 0
    instant = []
    for x in moves:
        x -= 1
        for y in range(len(board)):
            if board[y][x] != 0:
                instant.append(board[y][x])
                board[y][x] = 0
                if instant[-1:] == instant[-2:-1]:
                    answer += 2
                    instant = instant[:-2]
                break
    return answer