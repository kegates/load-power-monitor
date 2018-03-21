#include "EmonLib.h"
int inPinI;
int inPinV;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    inPinI = 1;
    inPinV = 2;
}

void loop(){
  
   
   double sampleI = analogRead(inPinI);
   double sampleV = analogRead(inPinV);

   Serial.print(sampleI);
   Serial.print(",");
   Serial.println(sampleV);
}


