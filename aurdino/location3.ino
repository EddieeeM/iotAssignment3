#include <math.h>
double Thermister(int RawADC) {
  double Temp;
  Temp = log(((10240000 / RawADC) - 10000));
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp )) * Temp );
  Temp = Temp - 273.15;
  return Temp;
}
#define lightSensorPin A1


int lightSensorValue = 0;

void setup() {
  pinMode(lightSensorPin, INPUT);

  Serial.begin(115200);
}

void loop() {
  lightSensorValue = analogRead(lightSensorPin);
  serial_print();

  delay(5000);

}

void serial_print()
{
  Serial.print(Thermister(analogRead(0)));
  Serial.print(" ");
  Serial.println(lightSensorValue);
}
