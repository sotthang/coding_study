def solution(s):
    answer = 0
    
    for x in s:
        if answer < 0:
            break
        answer = answer+1 if x == "(" else answer-1 if x == ")" else answer
    return answer==0