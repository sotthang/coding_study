while True:
	n = int(input())
	if n == 0:
		break
	n -= 1
	print("{", end=" ")
	i = 0
	while n != 0:
		if n % 2:
			print(3**i, end=", " if n // 2 else " ")
		n //= 2
		i += 1
	print("}")