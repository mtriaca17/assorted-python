def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			print(i)
			if alist[i]>alist[i+1]:
				print(f'array is: {alist}')
				print(f'pre sort number1: {alist[i]}, number2: {alist[i+1]}')
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
			print(f'post sort number1: {alist[i]}, number2: {alist[i+1]}')
			print(f'array is now: {alist}')

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)