def solution(numbers):
    answer = []
    for x in range(len(numbers)):
        for y in numbers[x+1:]:
            answer.append(numbers[x]+y)
    return sorted(list(set(answer)))