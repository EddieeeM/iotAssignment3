import json
import sys
import logging
from datetime import datetime
import pymysql


def check_data(dbConn) :
    cursor = dbConn.cursor()
    cursor.execute("SELECT temperature,light from templight ORDER BY id DESC LIMIT 1;")
    result = cursor.fetchall()
    for row in result :
        temp = float(row[0])
        light = float(row[1]) 
    if (temp >10.0 and light < 200.0) :
        ans = "lightfan"
    elif (light <200.0) :
        ans = "light"
    elif (temp > 10.0 ) :
        ans ="fan"
    else :
        ans= "off"
    return ans


def lambda_handler(event ,context) :
    dbConn = pymysql.connect("sensordata1.ccnxzgpssokn.us-east-1.rds.amazonaws.com","admin","password","sensor_data") or die("COuld not connect to the db")
    print(dbConn)
    result = check_data(dbConn)
    dbConn.close()
    return {
        'statusCode' : 200,
        'body' : json.dumps(result)
    }
	
