alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(int(input())):
    ans = 0
    s = input()
    for x in alpha:
        if x not in s:
            ans += ord(x)
    print(ans)