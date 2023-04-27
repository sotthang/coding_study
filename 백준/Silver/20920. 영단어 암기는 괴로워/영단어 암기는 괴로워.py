import sys

N, M = map(int,input().split())
d = {}
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    if len(s)<M:
        continue
    if s not in d:
        d[s]=[1,len(s),s]
    else:
        d[s][0]+=1
for _,_,s in sorted([*d.values()], key=lambda x:(-x[0],-x[1],x[2])):
    print(s)