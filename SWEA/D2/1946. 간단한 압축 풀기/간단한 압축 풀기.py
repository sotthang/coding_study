T = int(input())
for test_case in range(1, T + 1):
    s = ''
    for _ in range(int(input())):
       w, n = input().split()
       s += w*int(n)
    print(f'#{test_case}')
    for x in range((len(s)//10)+1):
        print(s[10*x:10*(x+1)])