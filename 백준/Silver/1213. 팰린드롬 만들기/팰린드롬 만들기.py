from collections import Counter

name = sorted(list(map(str, input())))
count = Counter(name)
odd = 0
odd_alpha = ""
ans = ""
for x in count:
    if count[x] % 2 != 0:
        odd += 1
        odd_alpha += x
    for _ in range(count[x] // 2):
        ans += x

if odd > 1:
    print("I'm Sorry Hansoo")
elif odd == 0:
    print(ans + ans[::-1])
else:
    print(ans + odd_alpha + ans[::-1])
