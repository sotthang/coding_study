def solution(s):
    return [-1 if s[:x][::-1].find(s[x]) == -1 else s[:x][::-1].find(s[x])+1 for x in range(0, len(s))]