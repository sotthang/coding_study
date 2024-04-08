n = input()
lst = [0]*26
for i in n:
    lst[ord(i)-97] += 1
for x in lst:
    print(x, end=' ')