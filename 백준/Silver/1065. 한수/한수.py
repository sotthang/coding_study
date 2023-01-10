count = 0
for num in range(1, int(input())+1):
    if num < 100:
        count += 1
    elif num%10 - num//10%10 == num//10%10 - num//100:
        count += 1
print(count)