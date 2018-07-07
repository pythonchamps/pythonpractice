
import pymysql

class MyException(Exception):
    def __init__(self,message="Default Message"):
        self.message = message

try:
    file = open("CityDump.csv","r")
    #raise MyException

    db = pymysql.connect(host = "localhost", user='root', password = 'tcs123Ion!@#', db="world")
    cursor = db.cursor()
    for x in file:
        x = x.strip()
        # print(x)
        lstX = x.split(",")
        # print(lstX[4])
        if (int(lstX[4]) >= 1000000):
            cursor.execute("Insert into citydemo(cityName,cityPop) values ({},{})".format(lstX[1], lstX[4]))

except pymysql.err.OperationalError:
    print("Database not connected. | Operational Error|")

except pymysql.err.ProgrammingError as e:
    print(format(e))
    print("Error in executing query")

except NameError:
    print("Variable was not found")

except pymysql.err.InternalError as e:
    print(format(e))
    print("Internal error")

except FileNotFoundError:
    print("File not found")

except MyException as e:
    print(format(e))
    print("My Exception")

except AssertionError as e:
    print(format(e))
    print("Assertion Error")
except IndexError:
    print("Index Error")

#except:
 #   print("Default Exception")

else:
    print("No Excpetion was raised")
    db.commit()

finally:
    pass
    #db.close()
    #file.close()