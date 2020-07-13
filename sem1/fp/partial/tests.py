from operations import*
def test_add():
	db = []
	add(db, '1','2', 'A', 'A') 
	assert db == [['1','2', 'A', 'A']]
	add(db,'2','3', 'B', 'A')
	assert db == [['1','2', 'A', 'A'], ['2','3', 'B', 'A']]
	add(db, '2', '5', 'C', 'D')
	assert db == [['1','2', 'A', 'A'], ['2','3', 'B', 'A'], ['2', '5', 'C', 'D']]


def test_update():
	db = [['1', '2', 'A', 'A'], ['2','3', 'B', 'D']]
	update(db, '1', '5')
	assert db == [['1', '5', 'A', 'A'], ['2','3', 'B', 'D']]
	update(db, '2', '6')
	assert db == [['1', '5', 'A', 'A'], ['2','6', 'B', 'D']]
	update(db, '2', '7')
	assert db == [['1', '5', 'A', 'A'], ['2','7', 'B', 'D']]


def test_modi():
	db = [['1', '2', 'A', 'C']]
	modi(db, 'C', 'D')
	assert db == [['1', '5', 'A', 'D']]

def test_sort():
	db = [['1','4','B', 'B'], ['2','3', 'B', 'C']]
	sort(db) 
	assert db == [ ['2','3', 'B', 'C'],['1','4','B', 'B']]



def test_checkCode():
    assert checkCode([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 4) == True
    assert checkCode([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1) == False
    assert checkCode([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 6) == True

def test_checkDuration():
    assert checkDuration(10) == False
    assert checkDuration(15) == False
    assert checkDuration(21) == True

def test_checkLen():
    assert checkLen("12") == True
    assert checkLen("1") == True
    assert checkLen("adsd") == False
    assert checkLen("a") == True


def test_Init():

	AssertionError = None
	try:
		test_checkCode()
	except:
		print("Code failed")
		AssertionError = True
	try:
		test_add()
	except:
		print("Add failed")
		AssertionError = True
	
	try:
		test_update()
	except:
		print("update faild")
		AssertionError = True

	try:
		test_sort()
	except:
		print("Sort failed")
		AssertionError = True

	if AssertionError == None:
		print("All test passed")
	else:
		print("Some test failed")	
