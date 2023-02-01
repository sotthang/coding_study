def solution(lottos, win_nums):
    answer =[]
    if len(set(win_nums) & set(lottos)) == 6:
        answer.append(1)
        answer.append(1)
    elif len(set(win_nums) & set(lottos)) == 5:
        answer.append(1)
        answer.append(2)
    elif len(set(win_nums) & set(lottos)) == 4:
        if lottos.count(0) == 2:
            answer.append(1)
            answer.append(3)
        elif lottos.count(0) == 1:
            answer.append(2)
            answer.append(3)
        else:
            answer.append(3)
            answer.append(3)
    elif len(set(win_nums) & set(lottos)) == 3:
        if lottos.count(0) == 3:
            answer.append(1)
            answer.append(4)
        elif lottos.count(0) == 2:
            answer.append(2)
            answer.append(4)
        elif lottos.count(0) == 1:
            answer.append(3)
            answer.append(4)
        else:
            answer.append(4)
            answer.append(4)
    elif len(set(win_nums) & set(lottos)) == 2:
        if lottos.count(0) == 4:
            answer.append(1)
            answer.append(5)
        elif lottos.count(0) == 3:
            answer.append(2)
            answer.append(5)
        elif lottos.count(0) == 2:
            answer.append(3)
            answer.append(5)
        elif lottos.count(0) == 1:
            answer.append(4)
            answer.append(5)
        else:
            answer.append(5)
            answer.append(5)
    elif len(set(win_nums) & set(lottos)) == 1:
        if lottos.count(0) == 5:
            answer.append(1)
            answer.append(6)
        elif lottos.count(0) == 4:
            answer.append(2)
            answer.append(6)
        elif lottos.count(0) == 3:
            answer.append(3)
            answer.append(6)
        elif lottos.count(0) == 2:
            answer.append(4)
            answer.append(6)
        elif lottos.count(0) == 1:
            answer.append(5)
            answer.append(6)
        else:
            answer.append(6)
            answer.append(6)
    else:
        if lottos.count(0) == 6:
            answer.append(1)
            answer.append(6)
        elif lottos.count(0) == 5:
            answer.append(2)
            answer.append(6)
        elif lottos.count(0) == 4:
            answer.append(3)
            answer.append(6)
        elif lottos.count(0) == 3:
            answer.append(4)
            answer.append(6)
        elif lottos.count(0) == 2:
            answer.append(5)
            answer.append(6)
        else:
            answer.append(6)
            answer.append(6)
    return answer