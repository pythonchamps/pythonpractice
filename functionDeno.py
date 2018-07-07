def sum(lst):
	sum = 0
	for x in lst:
		sum=sum+x
	return sum

x = sum([10,20,24])
y = sum((23,45,32))

print(x)
print(y)
print(sum(10))