chess = [list(input()) for _ in range(8)]
answer = 0
for i, x in enumerate(chess):
    if i % 2 == 0:
        answer += (x[0] + x[2] + x[4] + x[6]).count('F')
    else:
        answer += (x[1] + x[3] + x[5] + x[7]).count('F')
print(answer)