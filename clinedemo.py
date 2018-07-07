import sys

print ("Length of command line arguments is",len(sys.argv))
sum = 0

for i in range(1,len(sys.argv)):
	sum = sum + int(sys.argv[i])

print ("Sum is:", sum)

	
	