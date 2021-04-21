def pow_of_two(n):
	if n ==0:
		return 1
	else:
		return 2*pow_of_two(n-1)

print(pow_of_two(2))
print(pow_of_two(3))
print(pow_of_two(4))
print(pow_of_two(5))