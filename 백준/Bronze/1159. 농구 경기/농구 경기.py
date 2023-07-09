ln = {}
for _ in range(int(input())):
    s = input()[0]
    if s not in ln:
        ln[s] = 1
    else:
        ln[s] += 1
ans = "".join([k[0] for k in sorted(ln.items()) if k[1] >= 5])
print(ans) if ans else print("PREDAJA")