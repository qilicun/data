#!/usr/bin/env python

import sys
import argparse
import ert.ecl.ecl as ecl
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Read Ecl output files")
parser.add_argument('-e', '--eclfn', help="Name of ecl file", default=None, required=True)
parser.add_argument('-sw','--sw', help="extract sw", default=None, required=False)
parser.add_argument('-sg','--sg', help="extract sg", default=None, required=False)
parser.add_argument('-p', '--p',help="extract pressure", default=None, required=False)
parser.add_argument('-rv', '--rv',help="extract Rv", default=None, required=False)

args = parser.parse_args()

filen = ecl.EclFile(args.eclfn)
oil_sat = []
if args.sw:
    water_sat = np.array(filen["SWAT"][0])
    oil_sat = 1 - water_sat
    print "Water saturation:"
    print water_sat
if args.sg:
    gas_sat = np.array(filen["SGAS"][0])
    oil_sat = 1 - gas_sat
    print "Gas saturation:"
    print gas_sat
    
print "Oil saturation"
print oil_sat
#press = np.array(filen["PRESSURE"][0] * 6894.75729)

#print swat
#print press


