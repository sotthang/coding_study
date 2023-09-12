import sys

N = int(sys.stdin.readline())
target_str = sys.stdin.readline()
ans = 0
for alpha_str in [sys.stdin.readline() for _ in range(N - 1)]:
    if (
        abs(len(alpha_str) - len(target_str)) > 1
        or len(set(target_str).difference(set(alpha_str))) > 1
    ):
        continue
    for t in target_str:
        if t in alpha_str:
            alpha_str = alpha_str.replace(t, "", 1)
    if len(alpha_str) <= 1:
        ans += 1
print(ans)