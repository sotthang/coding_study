import math

def solution(my_str, n):
    return [my_str[x*n:x*n+n] for x in range(math.ceil(len(my_str)/n))]