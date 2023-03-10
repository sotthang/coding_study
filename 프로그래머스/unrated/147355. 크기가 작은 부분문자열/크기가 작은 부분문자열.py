def solution(t, p):
    answer = 0
    n = len(p)
    for x in range(len(t)-n+1):
        if int(p) >= int(t[x:x+n]):
            answer += 1
    return answer