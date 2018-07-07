for r in range(1,6):
	for c in range(1,6):
		if(r%5>1):
			if(c%5>1):
				print(" ", end = ' ')
			else:
				print("*", end = ' ')
		else:
			print("*",end = ' ')
	print("")