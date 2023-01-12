def solution(keyinput, board):
    answer = [0, 0]
    for x in keyinput:
        if x == "up" and (answer[1] < board[1]//2):
            answer[1] += 1
        elif x == "down" and (answer[1] > -board[1]//2+1):
            answer[1] -= 1
        elif x == "left" and (answer[0] > -board[0]//2+1):
            answer[0] -= 1
        elif x == "right" and (answer[0] < board[0]//2):
            answer[0] += 1
        print(x, answer)
    return answer