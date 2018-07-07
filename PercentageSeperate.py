def calc_percentage(lst):
    sum = 0.0
    per = 0.0
    for x in lst:
        sum += float(x) #sum=sum+x
    per = sum/len(lst)
    return per

def sort_list(lst):
    n = len(lst)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if(lst[j][2]>lst[j+1][2]):
                lst[j],lst[j+1] = lst[j+1],lst[j]

#Read The file
file = open("practice.csv","r")
result = open("result2.txt","a")

above60 = []
bet5060 = []
below50 = []

for line in file:
    line = line.strip()
    lst = line.split(",")
    per = calc_percentage(lst[2:])
    if(per>=60):
        above60.append([lst[0],lst[1],per])
    elif (per<60 and per>=50):
        bet5060.append([lst[0],lst[1],per])
    else:
        below50.append([lst[0],lst[1],per])

sort_list(above60)
sort_list(bet5060)
sort_list(below50)

result.write("\nTotal {} students scored more than or equal to 60%\n".format(len(above60)))
result.write("The Students Are: \n")
for x in above60:
    result.write(x[0] + " " +  x[1] + " " + str(x[2]) + "\n")

result.write("\nTotal {} students scored more than or equal to 50% and less than 60%".format(len(bet5060)))
result.write("The Students Are: \n")
for x in bet5060:
    result.write(x[0] + " " +  x[1] + " " + str(x[2]) + "\n")

result.write("\nTotal {} students scored less than 50%".format(len(below50)))
result.write("The Students Are: \n")
for x in below50:
    result.write(x[0] + " " +  x[1] + " " + str(x[2]) + "\n")

result.close()
file.close()