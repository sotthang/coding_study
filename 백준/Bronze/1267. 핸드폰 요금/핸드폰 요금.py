n = int(input())
n_list = list(map(int, input().split()))
y, m = 0, 0
for x in n_list:
    y += (1+x//30)*10
    m += (1+x//60)*15
if y==m:
    print(f'Y M {y}')
elif y < m:
    print(f'Y {y}')
else:
    print(f'M {m}')