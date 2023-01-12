s = input().upper()

answer = ''
c = 0
for char in set(s):
    if s.count(char) > c:
        c = s.count(char)
        answer = char
    elif s.count(char) == c:
        answer = '?'
print(answer)