def solution(array, height):
    answer = 0
    for x in array:
        if height < x:
            answer += 1
    return answer