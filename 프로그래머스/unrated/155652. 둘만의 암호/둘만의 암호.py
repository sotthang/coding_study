def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for x in skip:
        alphabet = alphabet.replace(x, '')
    for y in s:
        answer += alphabet[(alphabet.find(y)+index)%len(alphabet)]
    return answer