/*
  Arrays

  Demonstrates the use of an array to hold pin numbers in order to iterate over
  the pins in a sequence. Lights multiple LEDs in sequence, then in reverse.

  Unlike the For Loop tutorial, where the pins have to be contiguous, here the
  pins can be in any random order.

  The circuit:
  - LEDs from pins 2 through 7 to ground

  created 2006
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Array
*/

//int timer = 100;           // The higher the number, the slower the timing.
int buttonPins[] = {8, 9, 10, 11};       // an array of pin numbers to which LEDs are attached
int pinCount = 4;           // the number of pins (i.e. the length of the array)
int ButtonsState[4];
int index;
int ButtonValue;

void setup() {
  Serial.begin(9600);

  // the array elements are numbered from 0 to (pinCount - 1).
  // use a for loop to initialize each pin as an output:
  for (int index = 0; index < pinCount; index++) {
    pinMode(buttonPins[index], INPUT_PULLUP);
    ButtonsState[index] = digitalRead(buttonPins[index]);

//    ButtonsState[index] = ButtonValue;
  }
//  Serial.print("end setup");

}

void loop() {
  Serial.println();
  // loop from the lowest pin to the highest:
  for (int index = 0; index < pinCount; index++) {
    // turn the pin on:
    ButtonValue = digitalRead(buttonPins[index]);
//    Serial.println("buttonPins[index]: " + String(buttonPins[index]));
//    Serial.println("ButtonsState[index]: " + String(ButtonsState[index]));
//    Serial.println("ButtonValue: " + String(ButtonValue));
    
    if (ButtonValue != ButtonsState[index]) {
          Serial.print("this button has changed:");
          Serial.println(buttonPins[index]);

          // update state:
          ButtonsState[index] = ButtonValue;
       }
//    else {
//      Serial.println(buttonPins[index]);
//      Serial.println(ButtonValue);
//    }


  }
  
  delay(1000);


  // loop from the highest pin to the lowest:
//  for (int thisPin = pinCount - 1; thisPin >= 0; thisPin--) {
//    // turn the pin on:
//    digitalWrite(ledPins[thisPin], HIGH);
//    delay(300);
//    // turn the pin off:
//    digitalWrite(ledPins[thisPin], LOW);
//  }
}
