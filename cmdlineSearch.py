import sys
import pymysql
from importDB import db

if(len(sys.argv)<2):
    print("Invalid Arguments")
else:
    word_to_search = sys.argv[1]
    cursor = db.cursor()
    result_count = cursor.execute\
        ("select * from citydemo where cityname like '%{}%'".
         format(word_to_search))
    if(result_count == 0):
        print("No Records Found")
    else:
        print("{} records were found".format(result_count))
        data_all = cursor.fetchall()
        for x in data_all:
            print(" ".join(map(str,x)))





