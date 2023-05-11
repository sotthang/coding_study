answer = ''
for x in input():
    if x.isupper():
        answer += x.lower()
    else:
        answer += x.upper()
print(answer)