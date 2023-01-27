def solution(n, arr1, arr2):
    answer = []
    for arr_1, arr_2 in zip(arr1, arr2):
        count = ""
        arr1_binary = "{0:b}".format(arr_1).zfill(n)
        arr2_binary = "{0:b}".format(arr_2).zfill(n)
        for a, b in zip(arr1_binary, arr2_binary):
            if (a != "0") or (b != "0") :
                count += "#"
            else:
                count += " "
        answer.append(count)
    
    return answer