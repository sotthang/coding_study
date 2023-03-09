def solution(genres, plays):
    answer = []
    dict_genres1 = {}
    dict_genres2 = {}
    for z, (x, y) in enumerate(zip(genres, plays)):
        if x not in dict_genres1:
            dict_genres1[x] = [(z, y)]
        else:
            dict_genres1[x].append((z, y))
        if x not in dict_genres2:
            dict_genres2[x] = y
        else:
            dict_genres2[x] += y
    for (a, b) in sorted(dict_genres2.items(), key=lambda x:x[1], reverse=True):
        for (c, d) in sorted(dict_genres1[a], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(c)
    return answer