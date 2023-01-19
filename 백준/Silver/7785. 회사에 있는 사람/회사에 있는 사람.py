import sys

commute_dict = {}
for _ in range(int(sys.stdin.readline())):
    name, commute = sys.stdin.readline().rstrip().split()
    commute_dict[name] = commute
for name_enter in sorted(list(filter(lambda x:x[1]=='enter', commute_dict.items())), reverse=True):
    print(name_enter[0])