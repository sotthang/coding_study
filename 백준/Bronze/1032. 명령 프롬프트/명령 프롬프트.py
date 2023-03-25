li = [input() for _ in range(int(input()))]
answer = li[0]
for l in li[1:]:
    for x in range(len(answer)):
        if answer[x] != l[x]:
            answer = answer[:x] + '?' + answer[x+1:]
print(answer)