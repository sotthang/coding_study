def solution(array):
    answer = 0
    answer_count = 0
    array_list = []
    for x in set(array):
        array_list.append(array.count(x))
        if array.count(x) >= answer_count:
            answer_count = array.count(x)
            answer = x
    if array_list.count(max(array_list)) == 1:
        return answer
    else:
        return -1