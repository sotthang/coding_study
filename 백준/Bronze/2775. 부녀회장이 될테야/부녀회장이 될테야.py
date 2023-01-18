for test_case in range(1, int(input())+1):
    k = int(input())
    n = int(input())
    zero_floor = list(range(1, n+1))
    for floor in range(k):
        for room in range(1, n):
            zero_floor[room] += zero_floor[room-1]
    print(zero_floor[n-1])