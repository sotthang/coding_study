a, b, c = sorted(map(int, input().split()))
print(a+b+c) if a+b > c else print(a+b+a+b-1)