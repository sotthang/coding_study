n = int(input())
num = sorted(list(map(int, input().split())))
print(num[n // 2 - 1]) if n % 2 == 0 else print(num[n // 2])