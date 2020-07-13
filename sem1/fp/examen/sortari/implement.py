def suma(l):
	try:
		if len(l) <= 1:
			raise TypeError
	except TypeError:
		return("Not a list")
	try:
		s = 0
		for i in range(0, len(l)):
			if l[i]%2 == 0:
				s = s + l[i]
		if s == 0:
			raise ValueError
	except ValueError:
		return ("Not even")
	return s


'''
aux = [1]
print(suma(aux))
'''
'''
import unittest

class Test(unittest.TestCase):
	aux = [1,2,3]
	assert suma(aux) == 2
	aux = [1]
	assert suma(aux) == "Not a list"
	aux = [1,5,7]
	assert suma(aux) == "Not even"



if __name__ =='__main__':
	unittest.main()
'''
'''
def function(n):
	d = 2
	while (d < n - 1) and n % d > 0:
		d += 1
	print(d)
	return d >= n - 1

print(function(5))
'''

def Suma(data,s):
	if len(data) == 1:
		if data[0] % 2 == 0:
			s += data[0]
		return s
	mid = len(data)//2
	l1 = Suma(data[:mid], s)
	l2 = Suma(data[mid:], s)
	return (l1+l2)

aux = [2,2,2]
print(Suma(aux, 0))