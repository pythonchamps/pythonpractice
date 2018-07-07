import sys
import pymysql

if(len(sys.argv)<3):
    print("Invalid Values")
else:

    db = pymysql.connect(host = "localhost", user = "root", password="tcs123Ion!@#", db="world")
    cursor = db.cursor()

    records_found = cursor.execute ("select * from user where userid = '{}' and password = '{}'".format(sys.argv[1],sys.argv[2]))

    if(records_found ==1):
        print("Access Granted!!!")
    else:
        print("Access Denied!!!")

