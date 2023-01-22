def solution(s):
    answer = ''
    for x in s.split(' '):
        for i, y in enumerate(x):
            if i % 2 == 0:
                answer += y.upper()
            else:
                answer += y.lower()
        answer += ' '
    return answer[0:-1]
    