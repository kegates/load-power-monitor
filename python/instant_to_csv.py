import serial.tools.list_ports
import serial
import atexit
import time
import csv
import sys
from argparse import ArgumentParser

PORT = None

parser = ArgumentParser(description="Serial Port Parser")
parser.add_argument("-p", dest="port",
        help="port name", metavar="PORT")

args = parser.parse_args()

if args.port != None:
    PORT = args.port

def find_port_arduino():
    act_port = None
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if PORT in p[1]:
            act_port = p[0]
            print("Arduino found on port: " + act_port)
            break
    return act_port

def plot_and_update():
    port = find_port_arduino()
    if port is None:
        print("Error: No Arduino Connected")
        exit(1)

    ser = serial.Serial(port)
    
    
    print("Connection Open with Arduino On: " + ser.name)

    full_str = ""
    
    for i in range(0,500):
        line_str = ser.readline().decode('utf-8').replace('\r','')
        full_str = full_str + line_str

    ser.close()

    f = open('output.csv','w+')
    f.write("Current,Voltage\n")
    f.write(full_str)
    f.close()

   

   

if __name__ == "__main__":
    plot_and_update()
