#!/usr/bin/env python 

import argparse
import numpy as np
import matplotlib.pyplot as plt
import glob
parser = argparse.ArgumentParser(description="Ectract OPM wellrates")
parser.add_argument('-n', '--swn', help='Name of sw files', default=None,required=True)

args = parser.parse_args()

if args.swn:
    tmp = np.loadtxt(args.swn)
    sw = np.zeros(int(len(tmp)/3))
    so = np.zeros(int(len(tmp)/3))
    sg = np.zeros(int(len(tmp)/3))
    for i in xrange(len(sw)):
        sw[i] = tmp[3*i]
        so[i] = tmp[3*i+1]
        sg[i] = tmp[3*i+2]
    print "Water saturation:"
    print sw
    print "Oil saturation:"
    print so
    print "Gas saturation:"
    print sg
