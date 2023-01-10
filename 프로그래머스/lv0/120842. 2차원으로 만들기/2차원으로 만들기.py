def solution(num_list, n):
    return [num_list[n*x:n*x+n] for x in range(len(num_list)//n)]