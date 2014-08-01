#!/usr/bin/env python

import argparse
import numpy as np
import matplotlib.pyplot as plt
import linecache as lc
parser = argparse.ArgumentParser(description="Read Ecl output files")
parser.add_argument('-e', '--eclfn', help="Name of ecl file", default=None, required=True)

args = parser.parse_args()
filen = args.eclfn
swof=[]
sgof=[]
num = -1

def get_file_position(filen, string):
    pos = 0
    num = -1
    with open(filen, "r") as f:
        while True:
            num += 1
            line = f.readline()
            line = line.strip()
            if not len(line):
                continue
            line = line.split()
            if line[0]==string:
                pos = f.tell()    
                break
    return  pos
    
def get_line_number(filen, string):
    with open(filen, "r") as f:
        for num, line in enumerate(f.readline()):
            print f.tell()
            num += 1
            line = line.strip()
            if not len(line):
                continue
            line = line.split()
            if line[0]==string:
                break
    return num

def get_vec_values(filen, string):
    data = []
    position = get_file_position(filen, string)
    with open(filen, "r") as f:
        f.seek(position, 0)
        while True:
            line = f.readline()
            if not len(line):
                continue
            line = line.split()
            if line[-1] == "/":
                data += line[0:-1]
                break
            data += line
    return data


swof = get_vec_values(filen, "SWOF")
sgof = get_vec_values(filen, "SGOF")

swof = np.array(swof).reshape(len(swof)/4, 4)
sgof = np.array(sgof).reshape(len(sgof)/4, 4)
plt.figure(1)
plt.plot(swof[:,0], swof[:,1], linewidth=2)
plt.plot(swof[:,0], swof[:,2], linewidth=2)
plt.title("SWOF")
plt.figure(3)
plt.plot(swof[:,0], swof[:,3], linewidth=2)
plt.title("PCOW")
plt.figure(2)
plt.plot(sgof[:,0], sgof[:,1], linewidth=2)
plt.plot(sgof[:,0], sgof[:,2], linewidth=2)
plt.title("SGOF")
plt.show()
