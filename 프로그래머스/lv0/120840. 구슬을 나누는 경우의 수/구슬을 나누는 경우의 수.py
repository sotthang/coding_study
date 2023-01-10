def factorial(n):
    ans = 1
    for x in range(2, n+1):
        ans *= x
    return ans

def solution(balls, share):
    return factorial(balls) / (factorial(share) * factorial(balls-share))