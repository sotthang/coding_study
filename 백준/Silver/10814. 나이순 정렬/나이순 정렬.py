a_list = []
for _ in range(int(input())):
    age, name = map(str, input().split())
    a_list.append((int(age), name))
for n in sorted(a_list, key = lambda x:x[0]):
    print(n[0], n[1])