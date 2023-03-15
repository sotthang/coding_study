n = int(input())
print(sum([x*y for x, y in zip(sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())), reverse=True))]))