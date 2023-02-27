def solution(s):
    change_count, zero_delete_count = 0, 0
    while s != '1':
        change_count += 1
        zero_delete_count += s.count('0')
        s = bin(len(s.replace('0','')))[2:]
    return [change_count,zero_delete_count]