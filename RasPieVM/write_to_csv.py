import csv
import pymysql

#connection 
dbConn = pymysql.connect("sensordata1.ccnxzgpssokn.us-east-1.rds.amazonaws.com","admin","password","sensor_data") or die("COuld not connect to the db")
print(dbConn)
dbcursor = dbConn.cursor()

query = "SELECT * FROM templight;"
dbcursor.execute(query)

result = dbcursor.fetchall()
#export to csv

with open ("new_file.csv","w") as file :
    for row in result :
        csv.writer(file).writerow(row)

dbcursor.close()
del dbcursor

dbConn.close()

