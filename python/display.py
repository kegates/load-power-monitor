import serial.tools.list_ports
import serial
import atexit
import time
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd
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
    print(ports)
    for p in ports:
        if PORT in p[1]:
            act_port = p[0]
            print("Arduino found on port: " + act_port)
            break
    print(act_port)
    return act_port

def plot_and_update():
    port = find_port_arduino()
    if port is None:
        print("Error: No Arduino Connected")
        exit(1)

    ser = serial.Serial(port)
    
    
    print("Connection Open with Arduino On: " + ser.name)

    num_in_meas = 3
    c_lst = []
    v_lst = []
    a_pwr_lst = []
    current = 0.0
    voltage = 0.0
    app_power = 0.0

    for i in range(0,40):
        line_str = ser.readline().decode('utf-8', errors='replace').replace('\r','').replace('\n','')
        str_lst = line_str.split(" ")
        if len(str_lst) is not num_in_meas:
            continue
        (current, voltage, app_power) = list(map(float, str_lst))
        c_lst.append(current)
        v_lst.append(voltage)
        a_pwr_lst.append(app_power)

    dataset = list(zip(range(0,len(c_lst)),c_lst, v_lst, a_pwr_lst))
    df = pd.DataFrame(data=dataset, columns=['time', 'c_rms','v_rms','app_power'])
    print(df)

    ncols = 2
    nrows = 2
    sb.set_style("darkgrid")
    fig, axes = plt.subplots(nrows=2,ncols=2, sharex=True, sharey=False)
     
    ax1 = sb.pointplot(x="time",y="c_rms", data=df, ax=axes[0,0], markers="")
    ax2 = sb.pointplot(x="time", y="v_rms", data=df, ax=axes[0,1], markers="")
    ax3 = sb.pointplot(x="time",y="app_power",data=df, ax=axes[1,0], markers="")

    ax1.set_xticks([])
    ax1.set_xlabel("")
    ax2.set_xlabel("")
    ax3.set_xlabel("")


    print(type(ax1))
    plt.show()

    ser.close()

if __name__ == "__main__":
    plot_and_update()
