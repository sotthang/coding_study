def solution(s):
    answer = []
    for x in s.split():
        if x == 'Z':
            answer.pop()
        else:
            answer.append(int(x))
    return sum(answer)