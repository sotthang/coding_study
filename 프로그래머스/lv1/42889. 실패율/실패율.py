def solution(N, stages):
    answer = {}
    count = len(stages)
    for x in range(1, N+1):
        if count != 0:
            answer[x] = stages.count(x)/count
            count -= stages.count(x)
        else:
            answer[x] = 0
    
    return sorted(answer, key=lambda x : answer[x], reverse=True)