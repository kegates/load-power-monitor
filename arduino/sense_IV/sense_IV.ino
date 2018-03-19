// filename: sense_IV
// author: Kevin Gates
// ref: learn.openenergymoniter.com
// Has arduino read current and voltage
// and calculates values from this to serial output
// Each line of output is as follows in floats:
// <Amps RMS> <Assumed Voltage RMS> <Apparent Power>
// right now uses assumed voltage for resistive load.

#include "EmonLib.h"                   // Include Emon Library
EnergyMonitor emon1;                   // Create an instance

void setup()
{  
  Serial.begin(9600);
  
  emon1.current(1, 111.1);             // Current: input pin, calibration.
}

void loop()
{
  double Irms = emon1.calcIrms(1480);  // Calculate Irms only

  Serial.print(Irms);          // Irms
  Serial.print(" ");
  Serial.print("120");          //assumed Vrms
  Serial.print(" ");
  Serial.println(Irms*230.0);         // Apparent power
}
