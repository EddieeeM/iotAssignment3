
#include <DHT.h>

#include <math.h>

const int Fan = 3;
const int Temp_Sensor = 9;
const int Light_Sensor = A0;
float LightReading;
float Lux;
float TempReading;
float Temperature;
//float Threshold = 50;
String State = "ON";
String data = "";

void setup() 
{
  // Put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Fan, OUTPUT);
  pinMode(Temp_Sensor, INPUT);
  pinMode(Light_Sensor, INPUT);
}

void loop() 
{
  // Put your main code here, to run repeatedly:
  delay(1000);
  
  // Reading Values from sensors...
  LightReading = analogRead(Light_Sensor);
  // Lux = Light(LightReading);
  Lux = LightReading;

  TempReading = analogRead(Temp_Sensor);
  float Voltage = (TempReading * 3.3) / 1024.0; // Voltage

  Temperature = (Voltage - 0.5) * 100;         // Celsius
//  Temperature = (Voltage * 9.0 / 5.0) + 32.0;  // Farenheit
  
  Serial.println(Lux);            //Lux
  Serial.println(Temperature); //Temperature
  check_fan();
  /*
  if (Lux > Threshold)
  {
    digitalWrite(Fan, HIGH);
    State = "ON";
  } 
  else 
  {
    digitalWrite(Fan, LOW);
    State = "OFF";
  }
  */
}
void check_fan()
{
  if(Serial.available() > 0){
        data = Serial.readStringUntil('\n');
        //fan is on when vm send serial communication to on it
        if (data== "on") {
			digitalWrite(Fan, HIGH);
			State = "ON";
        }
        else  {
			digitalWrite(Fan, LOW);
			State = "OFF";
        }
        
    }
  
}

