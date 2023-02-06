def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for x in range(len(score)//m):
        answer += min(score[m*x:m*x+m]) * m
    return answer