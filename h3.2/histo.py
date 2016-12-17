def histo(s):
	#bir str in icindeki harfleri sayan program(bkz. histogram)
	res = {}
	s.lower
	for c in s:
		res[c] = res.get(c,0) + 1

	res = res.items()
	for pair in res:
		#print(pair)
		print("%s %-15d" % (pair))

s = input()
histo(s)
print(s)