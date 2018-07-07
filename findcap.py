import sys

if(len(sys.argv)<3):
    print("Invalid Arguments")

else:
    file = open(sys.argv[1],"r")
    words = sys.argv[2:]

    for line in file:
        line = line.lower()
        for w in words:
            line = line.replace(w.lower(),w.upper())
        print(line,end='')

