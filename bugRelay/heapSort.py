

def heapify(arr, n, i):
	largest = i 
	l = 3 * i + 1	 # '2*i + 1' changed to '3*i + 1'. The participants will need to know about the array implementation of heap sort to figure this out
	r = 4 * i + 2	 # '2*i + 2' changed to '4*i + 2'

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r > n and arr[largest] < arr[r]: # 'r < n' changed to 'r > n'
		largest = r


	if largest == i: # 'largest != i' changed to 'largest == i'
		arr[i], arr[largest] = arr[largest], arr[i]

	
		heapify(arr, n, largest)




def heapSort(arr):
	n = len(arr)

	
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0)



arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

