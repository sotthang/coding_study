def solution(dartResult):
    answer = list()
    dartResult = ['10' if x == 'k' else x for x in dartResult.replace('10', 'k')]
    bonus = ['S', 'D', 'T']
    index = -1
    
    for x in dartResult:
        if x in bonus:
            answer[index] = answer[index] ** (bonus.index(x)+1)
        elif x == '*':
            answer[index] = answer[index] * 2
            if index != 0:
                answer[index-1] = answer[index-1] * 2
        elif x == '#':
            answer[index] = -answer[index]
        else:
            answer.append(int(x))
            index += 1
    
    return sum(answer)