word = input()
for x in range(len(word)//10+1):
    print(word[10*x:10*x+10])