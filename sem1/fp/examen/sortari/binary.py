def BinarySearch(key, data, left, right):
	if left >= right-1:
		return right 
	middle = (left+right)//2
	if key < data[middle]:
		return BinarySearch(key, data, left, middle)
	else:
		return BinarySearch(key, data, middle, right)


def search(key, data):
	if len(data) == 0 or key < data[0]:
		return 0
	if key > data[-1]:
		return len(data)
	return BinarySearch(key, data, 0, len(data))

data = []

for i in range(0, 200):
	data.append(i)

print(BinarySearch(1, data, 0, len(data)))