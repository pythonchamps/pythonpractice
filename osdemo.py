import os

print(os.getcwd())

#cmd = os.popen("chrome www.gmail.com")

lst = os.listdir()


textlist = [x for x in lst if x.__contains__('.txt')]
print (textlist)
#print(cmd.read()