def solution(n):
    answer = set(range(2, n+1))

    for x in range(2, n+1):
        if x in answer:
            answer -= set(range(2*x, n+1, x))
    return len(answer)