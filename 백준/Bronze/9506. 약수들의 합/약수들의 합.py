while True:
    n = int(input())
    if n == -1:
        break
    ans = []
    for x in range(1, (n//2)+1):
        if n%x == 0:
            ans.append(x)
    if sum(ans) == n:
        print(f'{n} = ', end='')
        print(*ans, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')