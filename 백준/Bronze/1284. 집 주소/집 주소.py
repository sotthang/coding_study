while True:
    n = input()
    if n == '0':
        break
    ans = 0
    for x in n:
        if x == '1':
            ans += 3
        elif x == '0':
            ans += 5
        else:
            ans += 4
    print(ans+1)
