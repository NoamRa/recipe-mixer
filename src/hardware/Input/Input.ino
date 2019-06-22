
//recipe selection
const int X_pin = A1; // analog pin connected to X output

// texture
const int ledCount = 3;    // the number of LEDs in the bar graph
const int analogPin = A0;   // the pin that the potentiometer is attached to
int potState;

// colors
int buttonPins[] = {8, 9, 10};       // an array of pin numbers to which LEDs are attached
int pinCount = 3;           // the number of pins (i.e. the length of the array)
int ButtonsState[3];
int index;
int ButtonValue;

//random
int pushButton = 6;

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin 2 as an input and enable the internal pull-up resistor

//texture
  pinMode(2, INPUT_PULLUP);
  pinMode(3, OUTPUT);    // sets the digital pin 2 as output
  pinMode(4, OUTPUT);    // sets the digital pin 3 as output
  pinMode(5, OUTPUT);    // sets the digital pin 4 as output
  potState = analogRead(A0);

//colors
  for (int index = 0; index < pinCount; index++) {
    pinMode(buttonPins[index], INPUT_PULLUP);
    ButtonsState[index] = digitalRead(buttonPins[index]);
  }

//random
  pinMode(pushButton, INPUT);
  
}

//boolean for texture
boolean checkInRange(int x, int y, int range) {
  /*
   * check if "y" is close to "x" by "range"
   */
    int minValue = x - range;
    int maxValue = x + range;
    if (minValue <= y && y <= maxValue) {
      return false;
    }
    else {
      return true;
    }
}


void loop() {

  //read the pushbutton value into a variable
  //potentiometer loop
  int sensorVal = digitalRead(2);
  int potCurrent = analogRead(analogPin);
  int buttonState = digitalRead(pushButton);

  //recipe selection
  if ((analogRead(X_pin)) < 450){
    Serial.println("|down||");
  }

  if ((analogRead(X_pin)) > 600){
    Serial.println("|up||");
  }
  
  //int ledLevel = map(sensorReading, 0, 1023, 0, ledCount);    
  if (checkInRange(potState, potCurrent, 100)){
        potState = potCurrent;

    if ((potCurrent > 450) && (potCurrent < 600)){
            digitalWrite(4, LOW);
            digitalWrite(3, LOW);
            digitalWrite(5, LOW);
            Serial.print("|");
            Serial.print(potCurrent);
            Serial.println("||");  
            
        }
        else if (potCurrent < 512){
            digitalWrite(3, HIGH);
            digitalWrite(4, LOW);
            digitalWrite(5, LOW);
            Serial.print("|");
            Serial.print(potCurrent);
            Serial.println("||");
              
            } 
       
       else  if (potCurrent > 512){
            digitalWrite(5, HIGH);
            digitalWrite(3, LOW);
            digitalWrite(4, LOW); 
            Serial.print("|");
            Serial.print(potCurrent);
            Serial.println("||");

            }
        }
    
  

  //colors  loop from the lowest pin to the highest:
  for (int index = 0; index < pinCount; index++) {
      ButtonValue = digitalRead(buttonPins[index]);

      if (ButtonValue != ButtonsState[index]) {
          //Serial.print("this button has changed:");
          //Serial.println(buttonPins[index]);
          
          if (buttonPins[index] == 8) {
            Serial.print("|");
            Serial.print("Y");
            Serial.print("|");
            Serial.print(potCurrent);
            Serial.println("||");

          }
          else if (buttonPins[index] == 9) {
            Serial.print("|");
            Serial.print("B");
            Serial.print("|");
            Serial.print(potCurrent);
            Serial.println("||");
          }
      
          else if (buttonPins[index] == 10) {
            Serial.print("|");
            Serial.print("G");
            Serial.print("|");
            Serial.print(potCurrent);
            Serial.println("||");

          }
     
          ButtonsState[index] = ButtonValue;
      }
  }
  
  
  // Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
  // HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
  // button's pressed, and off when it's not:
  
        
      
//random
  if (buttonState == 1){
    Serial.print("|random");
    Serial.println("||");

  }
  
    delay(300);        // delay in between reads for stability
}

