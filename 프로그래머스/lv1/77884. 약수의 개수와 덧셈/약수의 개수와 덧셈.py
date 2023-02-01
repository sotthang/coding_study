def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        if (x ** (0.5)) != int(x ** (0.5)):
            answer += x
        else:
            answer -= x
    
    return answer