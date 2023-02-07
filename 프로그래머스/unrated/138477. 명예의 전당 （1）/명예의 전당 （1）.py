def solution(k, score):
    answer = []
    
    for x in range(len(score)):
        if x < k:
            answer.append(sorted(score[0:x+1], reverse=True)[x])
        else:
            answer.append(sorted(score[0:x+1], reverse=True)[k-1])
    
    return answer