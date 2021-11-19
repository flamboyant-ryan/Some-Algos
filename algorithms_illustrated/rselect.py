from quicksort import  partition
import random

arr = [7,67,87,45,88,88,12,1]


def rselect(arr,i):
	print(arr)
	if len(arr) == 1:
		return arr[0] 

	else:
		randompivot = random.randint(0, len(arr) - 1)
		arr[0], arr[randompivot] = arr[randompivot], arr[0]
		pivotpostion = partition(arr, 0, len(arr) - 1)
		
		if pivotpostion == i:
			return arr[i]
		elif pivotpostion > i:
			return rselect(arr[:pivotpostion], i)
		else:
			return rselect(arr[pivotpostion:], i - pivotpostion)

print(rselect(arr, 4))

print(sorted(arr))