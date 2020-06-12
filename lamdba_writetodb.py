import json
import sys
import logging
from datetime import datetime
import pymysql

def write_data(temp , light , location) :
    current = datetime.now()
    current_date = current.strftime("%d/%m/%Y")
    current_time = current.strftime("%H:%M:%S")
    cursor = dbConn.cursor()
    cursor.execute("INSERT into templight (temperature,light,location,date,time) Values(%s,%s,%s,%s,%s)" ,(temp,light,location,current_date,current_time))
    dbConn.commit()
    print(cursor.rowcount,"Value added to database.")
    cursor.close()
    
#connection 
dbConn = pymysql.connect("sensordata1.ccnxzgpssokn.us-east-1.rds.amazonaws.com","admin","password","sensor_data") or die("COuld not connect to the db")
print(dbConn)
dbcursor = dbConn.cursor()
#checking if there is already sensordata table if not creating one
query = "SHOW TABLES LIKE 'templight'; "
dbcursor.execute(query)
result = dbcursor.fetchall()
if result :
    print("table exists")
else :
    query1 = "CREATE TABLE templight(id INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY, temperature FLOAT(4) NOT NULL, light FLOAT(6) NOT NULL,location VARCHAR(20) NOT NULL,date VARCHAR(11) NOT NULL,time VARCHAR(11) NOT NULL);"
    dbcursor.execute(query1)
    ("Table created")


def lamda_handler (event ,context) :
    http_method = event ['httpMethod']
    if http_method == "GET" :
        temp = float(event['queryStringParameters']['temp'])
        light = float(event['queryStringParameters']['light'])
        location = event['queryStringParameters']['location']
    result = write_data(temp,light,location)
    db.close()
    return {
        'statusCode' : 200,
        'body' : json.dumps(result)
    }
