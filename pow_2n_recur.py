"""
This recursive function calculates 2ˆn by recursively
multiplying by 2 n-times. It terminates when the base case
n = 0 is reached.

"""

def pow_of_two(n):
	# base case
	if n ==0:
		return 1
	else:
		return 2*pow_of_two(n-1)
