#include <dht.h> 

#define lightSensorPin A0
#define tempPin  7
#define redled 4
#define blueled 5
#define greenled 6

dht DHT;
int lightSensorValue = 0;
int tempValue = 0;
String data = "off";

void setup() {
  pinMode(lightSensorPin,INPUT);
  pinMode(tempPin,INPUT);
  pinMode(redled,OUTPUT);
  pinMode(blueled,OUTPUT);
  pinMode(greenled,OUTPUT);
  Serial.begin(115200);
}

void loop() {
 DHT.read11(tempPin); 
 tempValue=DHT.temperature;
 lightSensorValue = analogRead(lightSensorPin);
 serial_print();
 check_led();
 delay(5000);

}

void serial_print()
{
  Serial.print(tempValue);
  Serial.print(" ");
  Serial.println(lightSensorValue);
}

void check_led()
{
  if(Serial.available() > 0){
        data = Serial.readStringUntil('\n');
        //light on the RBG led if signal is on else turn it off
        if (data== "on" || data== "fan_on" ) {
          digitalWrite(redled,HIGH);
          digitalWrite(blueled,HIGH);
          digitalWrite(greenled,LOW);
        }
        else  {
          digitalWrite(redled,LOW);
          digitalWrite(blueled,LOW);
          digitalWrite(greenled,LOW);
        }
        
    }
  
}
