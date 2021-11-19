def merge(arr1, arr2):
	lengthOfNewArr = len(arr1) + len(arr2)
	newArr = []

	i, j = 0, 0

	for k in range(lengthOfNewArr):
		if arr1[i:] and not arr2[j:]:
			newArr.extend(arr1[i:])
			break
			
		if not arr1[i:] and arr2[j:]:
			newArr.extend(arr2[j:])
			break
			
		if arr1[i:] and arr2[j:] and arr1[i] < arr2[j]:
			newArr.append(arr1[i])
			i += 1
			
		if arr1[i:] and arr2[j:] and arr2[j] < arr1[i]:
			newArr.append(arr2[j])
			j += 1
			
		

	return newArr

def mergesort(arr):
	if len(arr) <= 1:
		return arr
	return merge(mergesort(arr[:len(arr) // 2]), mergesort(arr[len(arr) // 2:]))


