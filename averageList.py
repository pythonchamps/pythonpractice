lst = []
sum = 0 

x = int(input("Enter No. of Elements"))

for n in range(x):
	lst.append(int(input("Enter No. ")))
	print(lst)
	

for i in lst:
	sum = sum + i

print("Average = ", sum/x)


