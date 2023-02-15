def solution(n):
    n_count = format(n, 'b').count('1')
    while True:
        n += 1
        if n_count == format(n, 'b').count('1'):
            return n