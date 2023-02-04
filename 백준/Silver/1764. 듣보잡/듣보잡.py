n, m = map(int, input().split())
dont_listen = {input() for _ in range(n)}
dont_look = {input() for _ in range(m)}
dont_listen_look = dont_listen & dont_look
print(len(dont_listen_look), *sorted(dont_listen_look), sep='\n')