def solution(num, total):
    answer = []
    if (total / num).is_integer():
        for x in range(((total // num) - num//2), ((total // num) + num//2) + 1):
            answer.append(x)
    else:
        for x in range(((total // num) - num//2) + 1, ((total // num) + num//2) + 1):
            answer.append(x)
    return answer