answer = 0
for _ in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        answer += 1
print(answer)