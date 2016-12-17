def reverse(s):
	"""
	>>> reverse('happy')
	'yppah'
	>>> reverse('Python')
	'nohtyP'
	>>> reverse("")
	''
	>>> reverse("P")
	'P'
	"""
	i = 1
	result = ""
	while i < len(s) + 1:
		result += s[-i]
		i += 1

	return result


def mirror(s):
	"""
	>>> mirror("good")
	'gooddoog'
	>>> mirror("yes")
	'yessey'
	>>> mirror('Python')
	'PythonnohtyP'
	>>> mirror("")
	''
	>>> mirror("a")
	'aa'
	"""
	return s + reverse(s)


def remove_letter(letter, strng):
	"""
	>>> remove_letter('a','apple')
	'pple'
	>>> remove_letter('a','banana')
	'bnn'
	>>> remove_letter('z','banana')
	'banana'
	>>> remove_letter('i','Mississippi')
	'Msssspp'
	"""

	result = ""
	for i in strng:
		if i != letter:
			result += i

	return result


def is_palindrome(s):
	"""
	>>> is_palindrome('abba')
	True
	>>> is_palindrome('abab')
	False
	>>> is_palindrome('tenet')
	True
	>>> is_palindrome('banana')
	False
	>>> is_palindrome('straw warts')
	True
	"""
	# if s == reverse(s):
	# 	return True
	# else:
	# 	return False
	for i in range(0,int(len(s)/2)):
		if s[i] != s[-(i+1)]:
			return False

	return True


def count(sub, s):
	"""
	>>> count('is', 'Mississippi')
	2
	>>> count('an', 'banana')
	2
	>>> count('ana', 'banana')
	2
	>>> count('nana', 'banana')
	1
	>>> count('nanan', 'banana')
	0
	"""
	count = 0
	for i in range(0, len(s)):
		if len(s) - i >= len(sub) and s[i] == sub[0]:
			if  s[i:len(sub)+i] == sub:
				count += 1

	return count


def remove_all(sub, s):
	"""
	>>> remove_all('an', 'banana')
	'ba'
	>>> remove_all('cyc', 'bicycle')
	'bile'
	>>> remove_all('iss', 'Mississippi')
	'Mippi'
	>>> remove_all('eggs', 'bicycle')
	'bicycle'
	"""
	i = 0
	while i < len(s):
		if len(s) - i >= len(sub):
			if  s[i:len(sub)+i] == sub:
				s = s[:i] + s[len(sub)+i:]
				break
		i += 1
	return s


def remove_all(sub, s):
	"""
	>>> remove_all('an', 'banana')
	'ba'
	>>> remove_all('cyc', 'bicycle')
	'bile'
	>>> remove_all('iss', 'Mississippi')
	'Mippi'
	>>> remove_all('eggs', 'bicycle')
	'bicycle'
	"""
	i = 0
	while i < len(s):
		if len(s) - i >= len(sub):
			if  s[i:len(sub)+i] == sub:
				s = s[:i] + s[len(sub)+i:]
				i -= 1
		i += 1
	return s


def replace(s, old, new):
	"""
	>>> replace('Mississippi', 'i', 'I')
	'MIssIssIppI'
	>>> s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
	>>> replace(s, 'om', 'am')
	'I love spam! Spam is my favorite food. Spam, spam, spam, yum!'
	>>> replace(s, 'o', 'a')
	'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!'
	"""
	i = 0
	while i < len(s):
		if len(s) - i >= len(old):
			if  s[i:len(old)+i] == old:
				s = s[:i] + new + s[len(old)+i:]
				i -= 1
		i += 1
	return s



if __name__ == '__main__':
	import doctest
	doctest.testmod()