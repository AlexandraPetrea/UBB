class A:
	def f(self, nr, l):
		l = l + [1]

class B:
	def g(self, nr, l):
		nr = nr + 1
		l = l.append(nr)
		return l

a = A()
b = B()
l = []
a.f(2,l)
b.g(2, l)
print(l)