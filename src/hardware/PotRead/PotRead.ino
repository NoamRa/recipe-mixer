
const int buttonPin = 2;     // the number of the pushbutton pin

int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);

}

// the loop routine runs over and over again forever:
void loop() {
  buttonState = digitalRead(buttonPin);
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  
//  int normalized = map(sensorValue, 0, 1024, -1, 1);

  if (buttonState == HIGH) {
    // print out the value you read:
    Serial.println(sensorValue);
  }
  else {
    Serial.println("none");
  }
  
  delay(100);        // delay in between reads for stability
}
