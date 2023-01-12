alphabet_dict = {x:-1 for x in 'abcdefghijklmnopqrstuvwxyz'}
for index, char in enumerate(input()):
    if alphabet_dict.get(char) == -1:
        alphabet_dict[char] = index

for num in alphabet_dict.values():
    print(num, end=' ')