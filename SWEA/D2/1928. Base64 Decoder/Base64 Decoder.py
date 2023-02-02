code = {s: i for i, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
T = int(input())
for test_case in range(1, T + 1):
    de = ''.join([format(code[x], 'b').zfill(6) for x in input()])
    en = ''.join([chr(int(de[8*x:8*x+8], 2)) for x in range(len(de)//8)])
    print(f'#{test_case} {en}')