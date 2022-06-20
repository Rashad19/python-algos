# This function calculates pisquared using the partial sum
# (1/6)*piˆ2 = sum from 1 to k of 1/kˆ2. This value is then used to
# calculate pi.


import math

def pisquared(n):

	result = 0.0
	i = 1.0;
	while(i<=n):
		result += 1/(i**2)
		i += 1

	pisquare = result*6.0

	return pisquare


def pi(n):

	pi = math.sqrt(pisquared(n))
	return pi
