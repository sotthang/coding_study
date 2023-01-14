def solution(array, n):
    array.sort()
    array_list = [abs(x - n) for x in array]
    return array[array_list.index(sorted(array_list)[0])]