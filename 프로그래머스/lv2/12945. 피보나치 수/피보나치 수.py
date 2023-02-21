def solution(n):
    f_list = [0, 1]
    for x in range(2, n+1):
        f_list.append(f_list[x-2] + f_list[x-1])
    return f_list[-1] % 1234567