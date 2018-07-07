file = open("result2.txt","a+")
x = file.tell()
file.write("This is the text that was added in append mode so is at the end of file")
y= file.tell()

print()