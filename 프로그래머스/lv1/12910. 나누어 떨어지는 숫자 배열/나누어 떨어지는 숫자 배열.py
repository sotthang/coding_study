def solution(arr, divisor):
    answer = []
    for x in sorted(arr):
        if x % divisor == 0:
            answer.append(x)
    if len(answer) > 0:
        return answer
    else:
        return [-1]