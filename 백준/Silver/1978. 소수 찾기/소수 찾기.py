test_case = int(input())
n = list(map(int, input().split()))
answer = len(n)
for num in n:
    if num == 1:
        answer -= 1
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            answer -= 1
            break

print(answer)