def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer.append([c+d for c, d in zip(a, b)])
    return answer