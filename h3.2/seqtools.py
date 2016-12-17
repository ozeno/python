def encapsulate(val, seq):
	if type(seq) == type(""):
		return str(val)
	if type(seq) == type([]):
		return [val]
	return (val,)


def insert_in_middle(val, seq):
	middle = len(seq)/2
	return seq[:middle] + encapsulate(val, seq) + seq[middle:]


def make_empty(seq):
	"""
	>>> make_empty([1, 2, 3, 4])
	[]
	>>> make_empty(('a', 'b', 'c'))
	()
	>>> make_empty("No, not me!")
	''
	"""
	if type(seq) == type(""):
		return str()
	if type(seq) == type([]):
		return []
	return ()


def insert_at_end(val, seq):
	"""
	>>> insert_at_end(5, [1, 3, 4, 6])
	[1, 3, 4, 6, 5]
	>>> insert_at_end('x', 'abc')
	'abcx'
	>>> insert_at_end(5, (1, 3, 4, 6))
	(1, 3, 4, 6, 5)
	"""
	return seq[:] + encapsulate(val, seq) 


def insert_in_front(val, seq):
	"""
	>>> insert_in_front(5, [1, 3, 4, 6])
	[5, 1, 3, 4, 6]
	>>> insert_in_front(5, (1, 3, 4, 6))
	(5, 1, 3, 4, 6)
	>>> insert_in_front('x', 'abc')
	'xabc'
	"""
	return encapsulate(val, seq) + seq[:]


def index_of(val, seq, start=0):
	"""
	>>> index_of(9, [1, 7, 11, 9, 10])
	3
	>>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
	3
	>>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
	6
	>>> index_of('y', 'happy birthday')
	4
	>>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
	1
	>>> index_of(5, [2, 3, 4])
	-1
	>>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
	-1
	"""
	i = start
	while i < len(seq):
		if seq[i] == val:
			return i
		i += 1
	return -1


def remove_at(index, seq):
	"""
	>>> remove_at(3, [1, 7, 11, 9, 10])
	[1, 7, 11, 10]
	>>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
	(1, 4, 6, 7, 0, 3, 5)
	>>> remove_at(2, "Yomrktown")
	'Yorktown'
	"""
	return seq[:index] + seq[index+1:]


def remove_val(val, seq):
	"""
	>>> remove_val(11, [1, 7, 11, 9, 10])
	[1, 7, 9, 10]
	>>> remove_val(15, (1, 15, 11, 4, 9))
	(1, 11, 4, 9)
	>>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
	('who', 'when', 'where', 'why', 'how')
	"""
	return remove_at(index_of(val, seq), seq)


def remove_all(val, seq):
	"""
	>>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
	[1, 7, 9, 10, 2]
	>>> remove_all('i', 'Mississippi')
	'Msssspp'
	>>> remove_all(11, (1, 7, 11, 9, 11, 10, 2, 11))
	(1, 7, 9, 10, 2)
	"""
	temp = []
	for i in seq:
		if i != val:
			temp += [i]

	if type(seq) == type(""):
		a = ""
		for i in temp:
			a += a.join(i)
		return a
	if type(seq) == type((0,)):
		return tuple(temp)
	return temp
	# indexes = []
	# for i, e in enumerate(seq):
	#  	if i == val:
	#  		indexes += [e]


def count(val, seq):
	"""
	>>> count(5, (1, 5, 3, 7, 5, 8, 5))
	3
	>>> count('s', 'Mississippi')
	4
	>>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
	2
	"""
	count = 0
	for i in seq:
		if i == val:
			count += 1
	return count
	


def reverse(seq):
	"""
	>>> reverse([1, 2, 3, 4, 5])
	[5, 4, 3, 2, 1]
	>>> reverse(('shoe', 'my', 'buckle', 2, 1))
	(1, 2, 'buckle', 'my', 'shoe')
	>>> reverse('Python')
	'nohtyP'
	"""
	temp = [0] * len(seq)
	for i, e in enumerate(seq):
		temp[-(i+1)] = e

	if type(seq) == type(""):
		a = ""
		for i in temp:
			a += a.join(i)
		return a
	if type(seq) == type((0,)):
		return tuple(temp)
	return temp


def sort_sequence(seq):
	"""
	>>> sort_sequence([3, 4, 6, 7, 8, 2])
	[2, 3, 4, 6, 7, 8]
	>>> sort_sequence((3, 4, 6, 7, 8, 2))
	(2, 3, 4, 6, 7, 8)
	>>> sort_sequence("nothappy")
	'ahnoppty'
	"""
	temp = []
	for i in seq:
		temp += [i]

	i = 1
	while i < len(temp):
		j = 0
		while j < len(temp) -i:
			if temp[j] > temp[j+1]:
				temp[j], temp[j+1] = temp[j+1], temp[j]
			j += 1
		i += 1

	if type(seq) == type(""):
		a = ""
		for i in temp:
			a += a.join(i)
		return a
	if type(seq) == type((0,)):
		return tuple(temp)
	return temp


if __name__ == "__main__":
	import doctest
	doctest.testmod()