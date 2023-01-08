def solution(n):
    lcm = 0
    for x in range(max(6, n), (6*n)+1):
        if x % 6 == 0 and x % n == 0:
            lcm = x
            break
    return lcm / 6