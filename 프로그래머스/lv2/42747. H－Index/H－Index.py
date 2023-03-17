def solution(citations):
    answer = 0
    for x in range(len(citations), -1, -1):
        temp = list(map(lambda y: y>=x, citations))
        if temp.count(True) >= x:
            answer = x
            break
    return answer