def solution(n):
    answer = 0
    for x in range(0, n+1):
        for y in range(2, x):
            if x%y==0:
                answer += 1
                break
    return answer