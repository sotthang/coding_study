def hanoi(n, s, e):
    if n == 1:
        answer.append([s, e])
        return
    hanoi(n-1, s, 6-s-e)
    answer.append([s, e])
    hanoi(n-1, 6-s-e, e)

def solution(n):
    hanoi(n, 1, 3)
    return answer

answer = []