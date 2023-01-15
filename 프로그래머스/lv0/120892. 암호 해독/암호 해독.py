def solution(cipher, code):
    return ''.join([cipher[code -1 + code*x] for x in range(0, len(cipher)//code)])