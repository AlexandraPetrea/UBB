def selectionSort(data):
	for i in range(0, len(data)-1):
		for j in range(i+1, len(data)):
			if data[j] < data[i]:
				data[i],data[j] = data[j], data[i]
	return data

def insertionSort(data):
	for i in range(1, len(data)):
		index = i - 1
		elem = data[i]
		while index >= 0 and elem < data[index]:
			data[index+1] = data[index]
			index = index -1
		data[index+1] = elem

def BubbleSort(data):
	done = False
	while not done:
		done = True
		for i in range(0, len(data)-1):
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				done = False
def bubble_sort_opt_n(data):
    n = len(data) - 1
    while n > 0:
        newn = 0
        i = 0
        while i < n: 
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                newn = i
            i += 1
        n = newn

def partition(data, left, right):
	pivot = data[left]
	i = left 
	j = right
	while i != j:
		while data[j] >= pivot and i <j:
			j -=1
		data[i] = data[j]
		while data[i] <= pivot and i < j:
			i += 1
		data[j] = data[i]
	data[i] = pivot
	return i
def QuickSort(data, left, right):
	pos = partition(data, left, right)
	if left < pos-1:
		QuickSort(data, left, pos-1)
	else:
		QuickSort(data, pos+1, right)

def merge_sort(l):
    if len(l) < 2:
        return l
        
    mid = len(l) // 2
    leftHalf = l[:mid]
    rightHalf = l[mid:]
    merge_sort(leftHalf)
    merge_sort(rightHalf)
    merge(leftHalf, rightHalf, l)

def merge(l1, l2, lrez):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
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
    lrez.clear()
    lrez.extend(l)
    
data = [1,4,5,3,2,6,0]
print(data)
#selectionSort(data)
insertionSort(data)
#BubbleSort(data)
#QuickSort(data, 0, len(data)-1)
#bubble_sort_opt_n(data)
#merge_sort(data)
print(data)