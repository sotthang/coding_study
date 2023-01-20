def solution(a, b):
    b,a = max(a, b), min(a, b)
    return sum(x for x in range(a, b+1))