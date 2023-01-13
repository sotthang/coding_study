def solution(score):
    answer = []
    for x in score:
        answer.append((x[0]+x[1])/2)
    return [sorted(answer, reverse=True).index(x)+1 for x in answer]