n = int(input())
hello_dict = {}
answer=0
for _ in range(n):
    s = input()
    if s == "ENTER":
        for k, v in hello_dict.items():
            if v == 1:
                answer += 1
        hello_dict = {}
    else:
        if s not in hello_dict:
            hello_dict[s] = 1
for k, v in hello_dict.items():
    if v == 1:
        answer+=1

print(answer)