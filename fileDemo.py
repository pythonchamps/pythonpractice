file = open('practice.csv','r')
names = []
marks = []
roll = []
for line in file:
    line = line.strip()
    lst = line.split(",")
    #print (lst[1])
    roll.append(int(lst[0]))
    names.append(lst[1])
    marks.append(int(lst[2]))

max = marks[0]
topperi = 0

for i in range(1, len(marks)):
    if(marks[i]>max):
        max = marks[i]
        topperi = i

print("Topper is ", names[topperi])
