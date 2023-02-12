def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

def solution(n):
    return fib(n+1) % 1000000007

