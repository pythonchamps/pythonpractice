import random
str=input("Enter between stone, paper and scissor ").lower()
a=["stone","paper","scissor"]
y=random.randint(1,3)
# print(y)
if(y==1):
	y="paper"
	print("randomly generated",y)
	if(str==a[0]):
		print("you lose")
	elif(str==a[1]):
		print("Draw , play again")
	else:
		print("You won")
	
if(y==2):
	y="stone"
	print("randomly generated",y)
	if(str==a[0]):
		print("draw,play again")
	elif(str==a[1]):
		print("you won")
	else:
		print("You lose")

if(y==3):
	y="scissor"
	print("randomly generated",y)
	if(str==a[2]):
		print("draw,play again")
	elif(str==a[1]):
		print("You lose")
	else:
		print("You won")
