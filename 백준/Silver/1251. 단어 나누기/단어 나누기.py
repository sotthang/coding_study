word = input()
word_len = len(word)
word_list = []
for x in range(1, word_len-1):
    for y in range(x+1, word_len):
        word_list.append(word[:x][::-1]+word[x:y][::-1]+word[y:][::-1])
print(sorted(word_list)[0])