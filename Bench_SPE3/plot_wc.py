#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

ecl = np.loadtxt('ecl_result/wr_prod')
opm = np.loadtxt('spe3_output/wr_prod')
#gor = np.loadtxt('gor')
#print wr[:,1] / (wr[:,1] + wr[:,2] + wr[:,3]+1e-20)
scale = 1#(1/30.48)**3*24*60*60
print "ECL well rates for producer"
print ecl.shape
print "opm well rates for producer"
opm[:,1]*=scale
opm[:,2]*=scale
opm[:,3]*=scale
print opm
plt.figure(1)
plt.plot(ecl[:,0], ecl[:,2] / (ecl[:,1] + ecl[:,2] +1e-30), linewidth=2)
plt.plot(opm[:,0], opm[:,2] / (opm[:,1] + opm[:,2] +1e-30), linewidth=2)
plt.legend(["ecl", "opm"])
plt.title('WCT')
plt.figure(2)
plt.plot(ecl[:,0], ecl[:,3]/(ecl[:,1]+1e-30), linewidth=2)
plt.plot(opm[:,0], opm[:,3]/(opm[:,1]+1e-30), linewidth=2)
plt.legend(["ecl", "opm"])
plt.title('GOR')
plt.show()

