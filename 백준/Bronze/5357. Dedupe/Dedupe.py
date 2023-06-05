for _ in range(int(input())):
    s = input()
    ans = s[0]
    for x in s[1:]:
        if ans[-1] != x:
            ans += x
    print(ans)