def listMap(lst,f):
	for x in range(len(lst)):
		lst[x] = f(lst[x])
	return lst



def square(x):
	return x**2

def cube(x):
	return x**3

if(__name__ == "__main__"):

	lst = [1,2,3,4,5]
	lst1 = [1,2,3,4,5]

	print(listMap(lst,square))

	print(listMap(lst1,cube))
