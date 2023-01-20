def solution(arr):
    answer = []
    for x in range(len(arr)-1):
        if arr[x] != arr[x+1]:
            answer.append(arr[x])
    answer.append(arr[-1])
    return answer