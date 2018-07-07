import pymysql
try:
    print("In Try Block")
    #File  = open("result.txt123",'r')
    db = pymysql.connect(host="localhost", user="root",password="root", db="world")

except pymysql.err.OperationalError as e:
    print(format(e))
    print("Database not connected")

else:
    print("In else block")

finally:
    print("Finally Block Executed")


