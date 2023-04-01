def solution(k, tangerine):
    answer = 0
    box = {}
    for i in tangerine:
        if i in box:
            box[i] += 1
        else:
            box[i] = 1
    box = dict(sorted(box.items(), key=lambda x: x[1], reverse=True))
    for j in box:
        if k <= 0:
            return answer
        k -= box[j]
        answer += 1
    return answer