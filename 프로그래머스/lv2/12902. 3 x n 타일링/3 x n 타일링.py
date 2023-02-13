def solution(n):
    answer = [3, 11]
    half_n = n//2
    
    if n == 2 or n == 4:
        return answer[half_n-1]
    
    for x in range(0, half_n-2):
        answer.append((answer[-1]*3+sum(answer[0:-1])*2+2)%1000000007)
    
    return answer[half_n-1]