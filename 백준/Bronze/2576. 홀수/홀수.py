num_list = list(filter(lambda x:x%2==1, [int(input()) for _ in range(7)]))
print(sum(num_list), min(num_list), sep='\n') if num_list else print(-1)