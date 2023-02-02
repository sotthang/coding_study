def solution(sizes):
    max_list = []
    min_list = []
    for x in sizes:
        max_list.append(max(x))
        min_list.append(min(x))
    return max(max_list) * max(min_list)