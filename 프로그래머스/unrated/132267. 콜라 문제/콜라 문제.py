def solution(a, b, n):
    answer = 0
    remain = 0
    while n >= a:
        answer += b*(n//a)
        if n%a == 0:
            n = n - a*n//a + b*(n//a)
        else:
            n = n - a*n//a + b*(n//a) + n%a
    return answer