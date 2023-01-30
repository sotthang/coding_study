li = [sum(list(map(int, input().split()))) for p in range(5)]
maximum = max(li)
print(li.index(maximum)+1, maximum)