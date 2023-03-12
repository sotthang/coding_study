def solution(cards1, cards2, goal):
    answer = 'Yes'
    for x in goal:
        if cards1 and x == cards1[0]:
            cards1.remove(x)
        elif cards2 and x == cards2[0]:
            cards2.remove(x)
        else:
            answer = 'No'
            break
    return answer