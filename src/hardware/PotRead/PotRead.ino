
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
//  int normalized = map(sensorValue, 0, 1024, -1, 1);

  // print out the value you read:
  Serial.println(sensorValue);
  delay(100);        // delay in between reads for stability
}
