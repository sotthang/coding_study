def solution(array, commands):
    answer = []
    for x in commands:
        a = array[x[0]-1:x[1]]
        a.sort()
        answer.append(a[x[2]-1])
    return answer