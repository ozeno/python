def add_lists(a, b):
	"""
	>>> add_lists([1, 1], [1, 1])
	[2, 2]
	>>> add_lists([1, 2], [1, 4])
	[2, 6]
	>>> add_lists([1, 2, 1], [1, 4, 3])
	[2, 6, 4]
	"""
	# iki listenin karsilikli elemanlarini toplayip baska bir liste olusturur.
	sum = []
	for i in range(len(a)):
		sum.append(a[i]+b[i])

	return sum


def mult_lists(a, b):
	"""
	>>> mult_lists([1, 1], [1, 1])
	2
	>>> mult_lists([1, 2], [1, 4])
	9
	>>> mult_lists([1, 2, 1], [1, 4, 3])
	12
	"""
	# iki listenin karsilikli elemanlarini carpip toplamlarini doner.(ic carpim)
	res =0
	for i in range(len(a)):
		res +=(a[i]*b[i])

	return res



if __name__ == '__main__':
	import doctest
	doctest.testmod()