def solution(sides):
    answer = 0
    for x in range(1, max(sides)+1):
        if max(sides) < min(sides) + x:
            answer += 1
    long = max(sides)+1
    while long < max(sides) + min(sides):
        answer += 1
        long += 1
    return answer