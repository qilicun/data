#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('spe1_output/gor')
ecl = np.loadtxt('spe1_output_before166/gor')

tmp =  data[:,2]/data[:,1]
np.savetxt('time.dat', data[:,0])
np.savetxt('gor.dat', tmp)
plt.plot(data[:,0], data[:,2]/data[:,1])
plt.plot(ecl[:,0], ecl[:,2]/ecl[:,1])
plt.ylim(215, 260)
plt.show()

