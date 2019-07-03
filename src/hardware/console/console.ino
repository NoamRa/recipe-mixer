
// LEDs
#include <Adafruit_NeoPixel.h>
#define LED_PIN 3
#define LED_COUNT 10
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

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
int randomPin = 2;
//int randomState = 0; 


void setup() {
  //start serial connection
  Serial.begin(9600);

  // LEDs
  strip.begin();
  strip.clear();
  strip.show();
  int brightness = 40; // (max = 255)
  strip.setBrightness(brightness); 
  updateDanger(512, false, false);

  //texture
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
  pinMode(randomPin, INPUT_PULLUP);
  
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
  
  boolean shouldUpdateDanger = false;
  boolean addColor = false;
  boolean doRandom = false;
  
  //recipe selection
  if ((analogRead(X_pin)) < 450){
    Serial.println("|down||");
  }

  if ((analogRead(X_pin)) > 600){
    Serial.println("|up||");
  }

  boolean potChanged = checkInRange(potState, potCurrent, 32);
  if (potChanged) {
    potState = potCurrent;
    Serial.print("|");
    Serial.print(potCurrent);
    Serial.println("||");
    shouldUpdateDanger = true;
  }
    
  //colors  loop from the lowest pin to the highest:
  for (int index = 0; index < pinCount; index++) {
    ButtonValue = digitalRead(buttonPins[index]);
    if (ButtonValue != ButtonsState[index]) {
      //Serial.print("this button has changed:");
      //Serial.println(buttonPins[index]);
      
      if (buttonPins[index] == 8) {
        Serial.print("|");
        Serial.print(potCurrent);
        Serial.println("|y||");
        shouldUpdateDanger = true;
        addColor = true;
      }
      else if (buttonPins[index] == 10) {
        Serial.print("|");
        Serial.print(potCurrent);
        Serial.print("|b||");
        shouldUpdateDanger = true;
        addColor = true;
      }
      else if (buttonPins[index] == 9) {
        Serial.print("|");
        Serial.print(potCurrent);
        Serial.print("|g||");
        shouldUpdateDanger = true;
        addColor = true;
      }
      ButtonsState[index] = ButtonValue;
    }
  }
  // Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
  // HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
  // button's pressed, and off when it's not:

  //random
  int randomState = digitalRead(randomPin);  // read input value

  if (randomState == LOW) {
//    Serial.println(randomState);
    Serial.println("|random||");
    shouldUpdateDanger = true;
    doRandom = true;
  }

  // handle RGB LEDs
  if (shouldUpdateDanger) {
      updateDanger(potCurrent, addColor, doRandom);
  }

  // delay in between reads for stability
  delay(300); 
}


void updateDanger(int potCurrent, boolean addColor, boolean doRandom) {
  uint32_t greenColor = strip.gamma32(strip.ColorHSV(26000));
  strip.setPixelColor(0, greenColor);
  
  if (doRandom) {
    showDanger(9);
//    Serial.println("Danger Zone! lvl 9");
    return;
  }
  
  int dangerLevel;
  if (potCurrent > 512) {
    dangerLevel = map(potCurrent, 512, 1023, 1, 9);
  }
  else if (potCurrent < 512){
    dangerLevel = map(potCurrent, 512, 0, 1, 9);
  }

  if (addColor) {
    int colorDangerFactor = 2;
    dangerLevel = min(dangerLevel + colorDangerFactor, 9);
  }

  showDanger(dangerLevel);
//  Serial.println("Danger Zone! lvl " + String(dangerLevel));
  return;
  
}

void showDanger(int dangerLevel) {
  //  dangerLevel is an int 1 to 9
  int hue = map(dangerLevel, 1, 9, 22000, 0);
  //  Serial.println("danger hue: " + String(hue));
  for (int idx = 1; idx < 9; idx++) {
    if (idx <= dangerLevel) {
      int saturation = 128;
      int value = 128;
      uint32_t color = strip.gamma32(strip.ColorHSV(hue));
      strip.setPixelColor(idx, color);
    }
    else {
      strip.setPixelColor(idx, 0, 0, 0);
    }
  }
  strip.show();
}

