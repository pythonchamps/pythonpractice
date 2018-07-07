import pymysql

class City:
    def __init__(self,id,name,ccode):
        self.id = id
        self.name = name
        self.ccode = ccode

    def __str__(self):
        return "CityName: {}, City ID: {} and Country Code: {}".format(self.name,self.id,self.ccode)

class CityMap:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='tcs123Ion!@#', db='world')
        self.cityList = []
        self.cityLength = 0

    def cityMap(self):
        cursor = self.db.cursor()
        dataLength = cursor.execute("select ID,Name,CountryCode from city")
        self.cityLength = dataLength
        dataAll = cursor.fetchall()
        for row in dataAll:
            self.cityList.append(City(row[0],row[1],row[2]))

    def cityDump(self):
        cursor = self.db.cursor()
        cursor.execute("select * from city")
        dataList = cursor.fetchall()
        #print(dataList)
        file = open("CityDump.csv","w")

        for x in dataList:
            #print(x)
            #print(str(x[0]) + "," + x[1] + "," + x [2] + "," + x[3] + "," + str(x[4]) +"\n")
            #file.write(ascii(str(x[0])) + "," + ascii(x[1]) + "," + ascii(x[2]) + "," + ascii(str(x[3])) +"\n")
            file.write(",".join(list(map(ascii,x))) + "\n")
    def getList(self):
        return self.cityList

    def getLength(self):
        return self.cityLength


cm = CityMap()
cm.cityDump()

