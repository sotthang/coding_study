import sys
import collections

n = int(sys.stdin.readline())
n_list = sorted([int(sys.stdin.readline()) for _ in range(n)])
cnt = collections.Counter(n_list).most_common()

print(round(sum(n_list)/n))
print(n_list[n//2])
if len(n_list) == 1 or cnt[0][1] != cnt[1][1]:
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
print(max(n_list)-min(n_list))