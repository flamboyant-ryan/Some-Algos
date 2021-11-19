import random
import mergesort
def choosePivot(left, right):
	return random.randint(left, right)

def partition(arr, left, right):
	i = left
	j = left
	while j < right:
		j += 1
		if arr[j] < arr[left]:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
			
			
	arr[i], arr[left] = arr[left], arr[i]
	return i

def quicksort(arr, left, right):
	if right - left <= 0:
		return 
	pivot = choosePivot(left, right)
	arr[pivot], arr[left] = arr[left], arr[pivot] # preprocessing
	part = partition(arr, left, right)
	quicksort(arr, left, part - 1)
	quicksort(arr, part + 1, right)

