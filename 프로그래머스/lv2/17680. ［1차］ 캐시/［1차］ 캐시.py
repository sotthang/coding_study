def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        c = city.lower()
        if c in cache:
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(c)
            answer += 5
    return answer