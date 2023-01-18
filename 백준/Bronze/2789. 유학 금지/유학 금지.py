word = list(input())
for w in 'CAMBRIDGE':
    while w in word:
        word.remove(w)
print(''.join(word))