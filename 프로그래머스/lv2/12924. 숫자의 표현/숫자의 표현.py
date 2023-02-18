def solution(n):
    answer = 0
    for x in range(1, n+1):
        count = 0
        while n > count:
            count += x
            x += 1
        if n == count:
            answer += 1
    return answer