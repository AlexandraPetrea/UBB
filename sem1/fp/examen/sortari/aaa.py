def merge_sort(l):
	if len(l) < 2:
		return l
	mid = len(l)//2
	left = l[mid:]
	right = l[:mid]
	merge_sort(left)
	merge_sort(right)
	merge(left, right, l)

def merge(l1, l2, rez):
	i = 0 
	j = 0 
	l = []
	while i < len(l1) and j < len(l2):
		if l1[i]< l2[j]:
			l.append(l1[i])
			i = i + 1
		else:
			l.append(l2[j])
			j = j + 1
	while i < len(l1):
		l.append(l1[i])
		i = i + 1
	while j < len(l2):
		l.append(l2[j])
		j = j + 1
	rez.clear()
	rez.extend(l)

data = [6,2,3,1,0,5]
#merge_sort(data)
#print(data)

def findMax(data):
	if len(data) == 1:
		return data[0]
	mid = len(data)//2
	left = findMax(data[:mid])
	right = findMax(data[mid:])
	return max(left, right)
#print(findMax(data))

def power(n, k):
	if k == 0:
		return 1
	if k == 1:
		return n
	aux = power(n, k//2)
	if k%2 == 0:
		return aux ** 2
	else:
		return aux * aux * n

print(power(2, 3))

from copy import deepcopy 
a = [1,2]
b = deepcopy(a)
b[1]= 8
print('a=',a)
print('b=', b)

class A:
	def f(self, l,nr):
		l.append(nr)
class B:
	def g(self, l, nr):
		nr=nr-1
		l = l+[-2]
a = A()
b = B()
l = [1,2]
c = -1
a.f(l,6)
b.g(l,c)
print(l,c)

a = lambda x: [x+1]
b = a(1)
c = lambda x: x + b
d = c([1])
a = 1
b = 3
print (a, b, c(4), d[1])
