def functieCuRaise(x):
	if x == 1:
		raise ValueError
	elif x == 2:
		raise TypeError
	elif x == 3:
		raise IOError
	return True

def testFunctieCuRaise():
	try:
		functieCuRaise(4)
		assert False
	except ValueError:
		assert True

	try:
		functieCuRaise(2)
		assert False
	except TypeError:
		assert True

	try:
		functieCuRaise(3)
		assert False
	except IOError:
		assert True

try:
	testFunctieCuRaise()
except AssertionError:
	print("Some test failed")