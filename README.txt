Project Name: power-sense-load-ac
Authors: Kevin Gates, Ryan Malley

Description:
    The purpose of this project is to poll an Arduino for real-time load power usage values (ac) in a Node Red Environment.
    There will be a node created to open/close serial with the Arduino, a node to poll the Aruino for updated values and
    store those into variables, and various nodes to call a get on each of those variables.  There will also be a sample
    node red program that opens a visual dashboard based on this data.

    The Arduino will print "Send 'D' to recieve real time values" to serial on opening of the port.  It will then send a line
    of values every time a 'D' is sent of the format "<realpower> <apparent power> <Vrms> <Irms> <power factor>"
    This can be seen in 'display.ino' in the Arduino subdirectory.

    The python file display.py can be seen for reference, but the python files and other unnused files will be remove upon completion
    of the project.  Likely a bash script will be used to initiate the node red environment, though python might also be used.

    In terms of setting up the circuit and Arduino, I intend to make a full github page on both that and usage of the nodes in node red.
