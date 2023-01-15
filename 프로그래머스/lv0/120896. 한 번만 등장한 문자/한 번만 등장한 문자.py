def solution(s):
    return "".join([x for x in "abcdefghijklmnopqrstuvwxyz" if s.count(x) == 1])