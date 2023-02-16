import sys

def is_promising(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            chess[x] = i
            if is_promising(x):
                n_queens(x+1)

n = int(sys.stdin.readline())
answer = 0
chess = [0] * n
n_queens(0)
print(answer)