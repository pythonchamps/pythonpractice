import pymysql
db = pymysql.connect(host = "localhost", user = "root", password = "tcs123Ion!@#", db = "world" )
if(__name__ == "__main__"):
    file = open("CityDump.csv","r")
    cursor = db.cursor()
    count = 0
    for x in file:
        x = x.strip()
        #print(x)
        lstX = x.split(",")
        #print(lstX[4])
        if(int(lstX[4])>=1000000):
            cursor.execute("Insert into citydemo(cityName,cityPop) values ({},{})".format(lstX[1],lstX[4]))
            count+=1

    db.commit()
    print(count)