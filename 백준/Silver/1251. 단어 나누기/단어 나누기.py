word = input()
word_len = len(word)
word_list = []
for x in range(1, word_len-2):
    for y in range(x+1, word_len-1):
        for z in range(y, word_len):
            word_list.append(word[:x][::-1]+word[x:z][::-1]+word[z:][::-1])
print(sorted(word_list)[0])