// the value of the 'other' resistor
#define SERIESRESISTOR 10000    
 
// What pin to connect the sensor to
#define THERMISTORPIN A0 

void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // declare 3 reading values:
  float reading;
  float reading2;
  float reading3;
 
  //Read one value from the arduino pin
  reading = analogRead(THERMISTORPIN);

  //Creation of 2 Mock readings
  reading2=2*reading;
  reading3=3*reading;


 // Print all 3 measurements on one line (IMPORTANT : All readings on the same line)
  Serial.print(reading);
  Serial.print(",");
  Serial.print(reading2);
  Serial.print(",");
  //Use Prinln to go to the new line after displaying last reading
  Serial.println(reading3);  
 
 // Delay before the loop starts again and record new measurements
  delay(1000); 
}