n, k = map(int, input().split())
people = [x for x in range(1, n + 1)]
t = 0
ans = []
while people:
    t = (t + k - 1) % len(people)
    ans.append(people.pop(t))
print(str(ans).replace("[", "<").replace("]", ">"))