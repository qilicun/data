#!/usr/bin/env python

f1 = 'spe3_output/wbhp'
f2 = 'ecl_result/wbhp'

import numpy as np

opm = np.loadtxt(f1)
ecl = np.loadtxt(f2)

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(opm[:,0], opm[:,1])
plt.plot(ecl[:,0], ecl[:,1]*6894.75729)
plt.title("WBHP-PROD")
plt.legend(["OPM", "ECL"])
plt.figure(2)
plt.plot(opm[:,0], opm[:,2])
plt.plot(ecl[:,0], ecl[:,2]*6894.75729)
plt.title("WBHP-INJE")
plt.legend(["OPM", "ECL"])
plt.show()
