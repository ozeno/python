# -*- coding: UTF-8 -*-

#calistirmak istetiginiz kismi yorum satirindan cikarin

x = 55
epsilon = 0.01
low = 0.0
high = max(x, 1.0)		#ust siniri en az 1 alarak sorunu cozduk
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
   print('ans =', ans, 'low =', low, 'high =', high)
   if ans**2 < x:
       low = ans
   else:
       high = ans
   ans = (high + low)/2.0
print(ans, 'is close to square root of', x)

#--------------------------------------------------

# x ve y nin farkinin epsilon dan fazla olup olmadigini kontrol eder
# def withinEpsilon(x, y, epsilon):
#    """x,y,epsilon ints or floats.  epsilon > 0.0
#       returns True if x is within epsilon of y"""
#    return abs(x - y) <= epsilon

# print(withinEpsilon(2,3,1))
# val = withinEpsilon(2,3,0.5)
# print(val)

#-------------------------------------

#x i 1 arttiran basit foksiyon ornegi
# def f(x):
#   x = x + 1
#   print('x =', x)
#   return x

# x = 3
# z = f(x)
# print('z =', z)
# print('x =', x)

#------------------------------------------

# def isEven(i):		#i nin cift olup olmadigini kontrol eder
#    """assumes i a positive int
#       returns True if i is even, otherwise False"""
#    return i%2 == 0

# def findRoot(pwr, val, epsilon):
#    """assumes pwr an int; val, epsilon floats
#       pwr and epsilon > 0
#       if it exists,
#          returns a value within epsilon of val**pwr
#          otherwise returns None"""
#    assert type(pwr) == int and type(val) == float\
#           and type(epsilon) == float
#    assert pwr > 0 and epsilon > 0		#assert yanindaki ifade False ise programin sonlanmasini
#    if isEven(pwr) and val < 0:		#saglar hatali calisacagina hic calismamasi daha iyi
#          return None

# karekok programinda yaptigimiz islemler ama artik farkli dereceden kokleri de bulabiliriz

#    low = -abs(val) 			# her durumda - x den
#    high = max(abs(val), 1.0)	# + x e kadarki araligi kontroletmek icin almamiz gereken degerler
#    ans = (high + low)/2.0
#    while not withinEpsilon(ans**pwr, val, epsilon):
#        #print( 'ans =', ans, 'low =', low, 'high =', high)
#        if ans**pwr < val:
#           low = ans
#        else:
#           high = ans
#        ans = (high + low)/2.0
#    return ans

# def testFindRoot():
#    """x float, epsilon float, pwr positive int"""
# -1 1 ve 3456 nin 1 2 ve 3 uncu derecelerden koklerini bularak programimizi test 
#	eden minik program (unit test)
#    for x in (-1.0, 1.0, 3456.0):
#        for pwr in (1, 2, 3):
#            ans = findRoot(pwr, x, 0.001)
#            if ans == None:
#                print('The answer is imaginary')
#            else:
#                print(ans, 'to the power', pwr,\
#                'is close to', x) 

# testFindRoot() #testi calistiralim 
