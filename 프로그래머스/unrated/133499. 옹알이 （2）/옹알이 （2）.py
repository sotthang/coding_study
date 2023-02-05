def solution(babbling):
    answer = 0
    anounce = ["aya", "ye", "woo", "ma"]
    for x in babbling:
        data = ''
        dont_continue = ''
        for y in x:
            data += y
            if dont_continue != data and data in anounce:
                dont_continue = data
                data = ''
        if len(data) == 0:
            answer += 1
    return answer