num_dict = {}
average = 0
for _ in range(10):
    n = int(input())
    if n not in num_dict:
        num_dict[n] = 1
    else:
        num_dict[n] += 1
for k, v in num_dict.items():
    average += k*v
print(average//10, sorted(num_dict.items(), key=lambda x:x[1], reverse=True)[0][0], sep='\n')