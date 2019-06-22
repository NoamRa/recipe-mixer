// Arduino pin numbers
//const int SW_pin = 2; // digital pin connected to switch output
const int X_pin = 1; // analog pin connected to X output
//const int Y_pin = 2; // analog pin connected to Y output

void setup() {
//  pinMode(SW_pin, INPUT);
// digitalWrite(SW_pin, HIGH);
  Serial.begin(9600);

}

void loop() {
//  Serial.print("Switch:  ");
//  Serial.print(digitalRead(SW_pin));
//  Serial.print("\n");
  if ((analogRead(X_pin)) < 500){
    Serial.println("|down||");
  }

  if ((analogRead(X_pin)) > 600){
    Serial.println("|up||");
  }

  delay(500);

}
