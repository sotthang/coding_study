t = int(input())
answer = 0
for y in input().split('0'):
    n = y.count('1')
    answer += (n*(n+1))//2
print(answer)