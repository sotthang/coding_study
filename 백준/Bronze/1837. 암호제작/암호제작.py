P, K = map(int, input().split())
answer = True
for x in range(2, K):
    if P % x == 0:
        print('BAD', x)
        answer = False
        break
if answer:
    print('GOOD')