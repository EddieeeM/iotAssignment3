import serial
import csv
import requests



	
	

def api_call(temp,light):
    location = "location1"
    link= "https://fezxb1dnk0.execute-api.us-east-1.amazonaws.com/default/writetodb?temp="+str(temp)+"&light="+str(light)+"&location="+location
    data = requests.get(link)
    result = data.text
    return result
   
    
    
ser = serial.Serial('/dev/ttyACM0',baudrate = 115200)

print("connected to :" + ser.portstr)

while 1 :
    reading = ser.readline().strip()
    allreading = reading.split( )
    temp = float(allreading[0])
    light = float(allreading[1])
    result = api_call(temp,light)
    print(result)