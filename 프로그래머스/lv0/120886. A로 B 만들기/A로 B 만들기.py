def solution(before, after):
    for x in before:
        if before.count(x) != after.count(x):
            return 0
    return 1