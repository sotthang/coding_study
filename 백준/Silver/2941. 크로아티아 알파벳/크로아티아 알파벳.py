n = input()
for x in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    n = n.replace(x, 'a')
print(len(n))