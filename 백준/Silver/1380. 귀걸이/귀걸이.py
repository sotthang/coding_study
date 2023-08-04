n = 1
while True:
    p = int(input())
    if p == 0:
        break
    student = [input() for _ in range(p)]
    li = [int(input().split()[0]) for _ in range(2 * p - 1)]
    print(n, student[[num for num in li if li.count(num) == 1][0] - 1])
    n += 1