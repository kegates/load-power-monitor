#include "EmonLib.h"
EnergyMonitor emon1;

double filteredV = 0;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    emon1.current(1, 111.1);
    emon1.voltage(2, 234.26,0);
    
}

void loop(){
   double lastFilteredV = filteredV;
  
   //long supply_v = emon1.readVcc();
   double sampleI = analogRead(emon1.inPinI);
   emon1.offsetI = (emon1.offsetI + (sampleI-emon1.offsetI)/1024);
   double filteredI = sampleI - emon1.offsetI;
   //Serial.println(filteredI);

   double sampleV = analogRead(emon1.inPinV);
   emon1.offsetV = (emon1.offsetV + (sampleV-emon1.offsetV)/1024);
   double filteredV = sampleV - emon1.offsetV; 
   double phaseShiftedV = lastFilteredV + emon1.PHASECAL * (filteredV - lastFilteredV);

   Serial.print(filteredV);
   Serial.print(" ");
   Serial.println(filteredI);
}


