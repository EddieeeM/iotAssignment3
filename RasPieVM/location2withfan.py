import serial
import csv
import MySQLdb
import pandas

device = "/dev/ttyACM0"

arduino = serial.Serial(device, 9600)

i = 0
x = 0

def checkdata():
	link= "https://6axn3pspr8.execute-api.us-east-1.amazonaws.com/default/control_fan_light"
	data = request.get(link)
	result = data.text
	if (result.find("fan") != -1) :
		ser.write("on".encode()) 
	else :
		ser.write("off".encode()) 
		
		
while i < 10:
    # Read Serialised Values
	checkdata()
    LightVal = arduino.readline()
    TemperatureVal = arduino.readline()
    
    # Conversion to readable format & Prints onto Terminal
    Lumens = LightVal.decode("utf-8")
    Celsius = TemperatureVal.decode("utf-8")
    print(Lumens)
    print(Celsius)
    
    # Removes /r /n at the end value...
    Lumens = LightVal[0:-2] 
    Celsius = TemperatureVal[0:-2]
   
    dbConn = MySQLdb.connect("localhost", "root", "root", "Assign3") or die("Unable to connect to Database")
    
    # Places 20 Values into the Database
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("INSERT INTO ValueHolder (Lumens, Celsius) VALUES (%s, %s)", (Lumens, Celsius))
        dbConn.commit()
    
    i += 1
else:
    
    print(dbConn)
    with dbConn:
        cursor.close();