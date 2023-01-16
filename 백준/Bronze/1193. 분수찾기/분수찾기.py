x = int(input())
n, count = 1, 0
while n + count < x:
    count += 1
    n += count
print(f'{count+1+n-x}/{1+x-n}') if count % 2 == 0 else print(f'{1+x-n}/{count+1+n-x}')