num = [1,2,3,4,5]

num_of_int = 5
rotations = 4

print('This is using array slicing')
shifted_array = num[rotations:] + num[:rotations] 

print(shifted_array)

print('\nThis is a loop that does the same thing so it shows one by one')
for i in range(1, rotations+1):
	x = num.pop(0)
	num.append(x)
	print(num)