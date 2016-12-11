def sqrt(n):
	approx = n/2.0
	better = (approx + n/approx)/2.0
	while better != approx:
		approx = better
		better = (approx + n/approx)/2.0
		print(better)

	return approx

def is_prime(n):
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1

	return True

print(is_prime(11))
print(is_prime(5))
print(is_prime(25))