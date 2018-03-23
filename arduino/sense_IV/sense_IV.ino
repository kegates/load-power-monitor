// filename: sense_IV
// author: Kevin Gates
// ref: learn.openenergymoniter.com
// Has arduino read current and voltage
// and calculates values from this to serial output

#include "EmonLib.h"             // Include Emon Library
EnergyMonitor emon1;             // Create an instance

void setup()
{  
  Serial.begin(9600);
  
  emon1.voltage(2, 120, 0);  // Voltage: input pin, calibration, phase_shift
  emon1.current(1, 60);       // Current: input pin, calibration.

  Serial.println("Send 'D' to recieve real time values.");
}

void loop()
{
  while(!Serial.available()){}
  char read = Serial.read();
  if(read == 'D'){
    emon1.calcVI(20,2000);         // Calculate all. No.of half wavelengths (crossings), time-out
    emon1.serialprint(); // Print out all variables (realpower, apparent power, Vrms, Irms, power factor)
  }
}
