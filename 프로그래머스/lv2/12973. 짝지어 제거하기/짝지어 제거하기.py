def solution(s): 
    answer = []
    for x in s:
        if len(answer) == 0 or answer[-1] != x:
            answer.append(x)
        else:
            answer.pop()
    return 1 if len(answer) == 0 else 0 