def solution(brown, yellow):
    answer = []
    for x in range(round((brown+yellow)**0.5), brown+yellow):
        if (max(x, (brown+yellow)//x)-2) * (min(x, (brown+yellow)//x)-2) == yellow:
            answer = [max(x, (brown+yellow)//x), min(x, (brown+yellow)//x)]
    return answer