def solution(spell, dic):
    for x in dic:
        answer = 0
        for y in spell:
            if x.count(y) == 1:
                answer += 1
        if len(spell) == answer:
            return 1
    return 2