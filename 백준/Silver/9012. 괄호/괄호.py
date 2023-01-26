for test_case in range(int(input())):
    ps = input()
    for x in range(len(ps)//2):
        ps = ps.replace('()', '')
    print('NO') if ps else print('YES')