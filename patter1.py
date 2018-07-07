r=5
while(r>=1):
	c=1
	while(c<=r):
		if (r%2!=0):
			print("*", end = ' ')
		else:
			print("-", end = ' ')
		c = c+1
	r = r - 1
	print("") 
		
