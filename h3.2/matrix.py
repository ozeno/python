def make_matrix(rows, columns):
	"""
	>>> make_matrix(3, 5)
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	>>> make_matrix(4, 2)
	[[0, 0], [0, 0], [0, 0], [0, 0]]
	>>> m = make_matrix(4, 2)
	>>> m[1][1] = 7
	>>> m
	[[0, 0], [0, 7], [0, 0], [0, 0]]
	"""
	matrix = []
	for row in range(rows):
		matrix += [[0] * columns]
		
	return matrix


def add_row(matrix):
	"""
	>>> m = [[0, 0], [0, 0]]
	>>> add_row(m)
	[[0, 0], [0, 0], [0, 0]]
	>>> n = [[3, 2, 5], [1, 4, 7]]
	>>> add_row(n)
	[[3, 2, 5], [1, 4, 7], [0, 0, 0]]
	>>> n
	[[3, 2, 5], [1, 4, 7]]
	"""
	l = len(matrix[0])
	temp = matrix[:]
	temp += [[0]*l]
	return temp


def add_column(matrix):
	import copy
	"""
	>>> m = [[0, 0], [0, 0]]
	>>> add_column(m)
	[[0, 0, 0], [0, 0, 0]]
	>>> n = [[3, 2], [5, 1], [4, 7]]
	>>> add_column(n)
	[[3, 2, 0], [5, 1, 0], [4, 7, 0]]
	>>> n
	[[3, 2], [5, 1], [4, 7]]
	"""
	# temp = []
	# for e in matrix:
	# 	temp_in = []
	# 	for i in e:
	# 		temp_in += [i]
	# 	temp_in.append(0)
	# 	temp.append(temp_in)

	# return temp

	temp = copy.copy(matrix)
	for row in temp:
		row += [0]

	return temp

def add_matrices(m1, m2):
	"""
	>>> a = [[1, 2], [3, 4]]
	>>> b = [[2, 2], [2, 2]]
	>>> add_matrices(a, b)
	[[3, 4], [5, 6]]
	>>> c = [[8, 2], [3, 4], [5, 7]]
	>>> d = [[3, 2], [9, 2], [10, 12]]
	>>> add_matrices(c, d)
	[[11, 4], [12, 6], [15, 19]]
	>>> c
	[[8, 2], [3, 4], [5, 7]]
	>>> d
	[[3, 2], [9, 2], [10, 12]]
	"""
	
	temp = []
	for i in range(len(m1)):
		e = []
		for j in range(len(m1[0])):
			e.append(m1[i][j]+m2[i][j])
		temp.append(e)
	return temp


def scalar_mult(n, m):
	"""
	>>> a = [[1, 2], [3, 4]]
	>>> scalar_mult(3, a)
	[[3, 6], [9, 12]]
	>>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
	>>> scalar_mult(10, b)
	[[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
	>>> b
	[[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
	"""
	temp = []
	for i in range(len(m)):
		e = []
		for j in range(len(m[0])):
			e.append(m[i][j]*n)
		temp.append(e)
	return temp


def row_times_column(m1, row, m2, column):
	"""
	>>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]],0)
	19
	>>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]],1)
	22
	>>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]],0)
	43
	>>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]],1)
	50
	"""
	sum = 0
	for i in range(len(m1[0])):
		sum += (m2[i][column] * m1[row][i])
	return sum


def matrix_mult(m1, m2):
	"""
	>>> matrix_mult([[1, 2], [3, 4]], [[5, 6], [7, 8]])
	[[19, 22], [43, 50]]
	>>> matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 1],[2, 3]])
	[[31, 19], [85, 55]]
	>>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4,5, 6]])
	[[39, 54, 69], [13, 23, 33], [14, 19, 24]]
	"""
	temp = []
	for i in range(len(m1)):
		e = []
		for j in range(len(m2[0])):
			e.append(row_times_column(m1,i,m2,j))
		temp.append(e)
	return temp


if __name__ == '__main__':
	import doctest
	doctest.testmod()
