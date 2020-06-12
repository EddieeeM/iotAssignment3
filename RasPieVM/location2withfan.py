import serial
import csv
import requests

def checkdata():
	link= "https://6axn3pspr8.execute-api.us-east-1.amazonaws.com/default/control_fan_light"
	data = requests.get(link)
	result = data.text
	if (result.find("fan") != -1) :
		ser.write("on".encode()) 
	else :
		ser.write("off".encode()) 
		
def api_call(temp,light):
    location = "location2"
    link= "https://fezxb1dnk0.execute-api.us-east-1.amazonaws.com/default/writetodb?temp="+str(temp)+"&light="+str(light)+"&location="+location
    data = requests.get(link)
    result = data.text
    return result
    
arduino = serial.Serial('/dev/ttyACM0',baudrate = 9600)

print("connected to :" + arduino.portstr)

while 1 :
    checkdata()
    # Read Serialised Values
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
    
    temp = float(Celsius)
    light = float(Lumens)
    result = api_call(temp,light)
    print(result)
