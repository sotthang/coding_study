num_list = []
for x in range(1, 10001):
    a = x
    b = x
    while a/10 > 0:
        b += a%10
        a //= 10
    num_list.append(b)

for x in sorted(set(range(1, 10001))-set(num_list)):
    print(x)