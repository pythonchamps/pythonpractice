str1 = input("Enter Sub String ")
str2 = input("Enter Super String ")

if(str1.lower() in str2.lower()):
	print(str1 + " is part of  " + str2)
else:
	print(str1 + " is not part of " + str2)
