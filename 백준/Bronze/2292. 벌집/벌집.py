n = int(input())
house = 1
count = 1
while n > house:
    house += count * 6
    count += 1
print(count)