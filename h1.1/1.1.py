x = 3  
x = x*x  
print(x)
y = eval(input('enter a number:'))
print((type(y)))
print(y)
y = float(input('Enter a number: '))
print((type(y)))
print(y)
print((y*y))

x = int(input('Enter an integer: '))
if x%2 == 0:
	print('Even')
else:
	print('Odd')
	if x%3 != 0:
		print('And not divisible by 3')

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

#Sizce dogru calisir mi? 
if x < y:
	if x < z:
		print('x is least')
	else:
		print('z is least')
else:
	print('y is least')

#basit birkac foksiyon ornegi
def is_even(n):
	return n % 2 == 0

def is_odd(n):
	return not is_even(n)

def is_factor(n, m):		#n m yi tam bolerse bir capanidir.
	return m % n == 0

def is_multiple(n, m):
	return is_factor(m, n)

def slope(x1, y1,x2, y2):	#egim
	return abs((y1-y2)/float(x1-x2))

def test():
	print("Fonksiyonda...")
	if False: return
	print("hala burdayim...")
	if True: return
	print("bu satir calismayacak")
	print("bu da...")

#fonksiyon cagirimi
is_even(123)
is_odd(123)
is_factor(3, 15)
print("hello {}".format("world!"))	#burada print de format ta birer fonksiyondur.
print (test)
test()