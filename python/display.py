import serial.tools.list_ports
import serial
import atexit
import time


def find_port_arduino():
    act_port = None
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p[1]:
            act_port = p[0]
            print("Arduino found on port: " + act_port)
            break

    return act_port

def read_to_stdout():
    port = find_port_arduino()
    if port is None:
        print("Error: No Arduino Connected")
        exit(1)

    ser = serial.Serial(port)
    
    
    print("Connection Open with Arduino On: " + ser.name)
    for i in range(0,5):
        print(ser.readline())
    ser.close()

if __name__ == "__main__":
    read_to_stdout()
