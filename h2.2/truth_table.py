expression = input("Enter the expression: ")
print("p       q       %s" % expression)
l = len("p       q       %s" % expression)
print(l*"=")

for p in True, False:
	for q in True, False:
		print("%-7s %-7s %-7s" % ( p, q, eval(expression)))