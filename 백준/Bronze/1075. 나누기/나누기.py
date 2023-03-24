n = int(input())
f = int(input())
answer = '00'
while True:
    n = int(str(n)[:-2]+answer)
    if n%f == 0:
        break
    answer = str(int(answer)+1).zfill(2)
print(answer)