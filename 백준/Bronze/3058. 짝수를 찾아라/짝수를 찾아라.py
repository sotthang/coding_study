for _ in range(int(input())):
    x = list(filter(lambda x:x%2==0, list(map(int, input().split()))))
    print(sum(x), min(x))