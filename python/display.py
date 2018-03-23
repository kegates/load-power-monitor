import serial.tools.list_ports
import serial
import time
from argparse import ArgumentParser
import sys

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
    print(ports)
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
    
    ser.readline().decode('utf-8')
    #should check to make sure this is the proper start-up response

    print("Connection Open with Arduino On: " + ser.name)
    sys.stdout.flush()

    num_in_meas = 5
    a_pwr_lst = []
    r_pwr_lst = []
    r_pwr = 0.0
    a_pwr = 0.0
    Vrms = 0.0
    Irms = 0.0
    pf = 0.0

    #Should have a start and stop button on node red dashboard with sentinal value as opposed to infinite update loop
    #Will receive '<realpower> <apparentpower> <Vrms> <Irms> <pf>' each occurance upon sending 'D'
    for i in range(0,5):
        ser.write(b'D')
        line_str = ser.readline().decode('utf-8', errors='replace').replace('\r','').replace('\n','')
        str_lst = line_str.split(" ")
	#should use try catch block instead of this
        if len(str_lst) is not num_in_meas:
            continue
        (r_pwr, a_pwr, Vrms, Irms, pf) = list(map(float, str_lst))
        a_pwr_lst.append(a_pwr)
        r_pwr_lst.append(r_pwr) 
        print("test")
        #sys.stdout.flush()
        time.sleep(1)


    ser.close()

if __name__ == "__main__":
    plot_and_update()
