word = input()
answer = 1
for x in range(len(word)//2):
    if word[x] != word[-x-1]:
        answer = 0
print(answer)