def solution(n):
    answer = 1
    count = 1
    while n != count:
        count += 1
        answer += 1
        while (answer % 3 == 0) or ('3' in str(answer)):
            answer += 1
    return answer