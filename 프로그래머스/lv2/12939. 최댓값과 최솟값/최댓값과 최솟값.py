def solution(s):
    s = [int(x) for x in s.split()]
    return f"{min(s)} {max(s)}"