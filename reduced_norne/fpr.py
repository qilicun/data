#!/bin/env python

import numpy as np
import glob
import matplotlib.pyplot as plt
import os
##Get FPR from output/pressure/*.txt

def get_opm_pav(path):
    file = glob.glob(path+'*.txt')
    file.sort()
    tmp=[27000000]
    for i in file:
        p = np.loadtxt(i)
        tmp.append(np.array(p).mean())

    return np.array(tmp)

path="/project/eor/Norne/nornecase/reduced_norne/lrat_restart_output/pressure/"
if os.path.isfile('lrat_restart_output/opm_pav.txt'):
    opm_pav = np.loadtxt('lrat_restart_output/opm_pav.txt')
else:
    opm_pav = get_opm_pav(path)
    #write to file
    np.savetxt("lrat_restart_output/opm_pav.txt", opm_pav)

#load ecl result
ecl_pav = np.loadtxt("ecl_fpr.txt")

#set fixed time step
timestep=[0]+[1,2,3,4,5,5,10,10]+[20]*3#+[25]*8+[50]*34+[100]*80
dt=np.add.accumulate(timestep)

#do ploting, error bar and FPR line
plt.plot(dt, opm_pav/1e5, label='OPM')
#plt.plot(ecl_pav[:,0], ecl_pav[:,1], label='ECL_NO_NTG_NO_FAULTS')
plt.plot(ecl_pav[:,0], ecl_pav[:,1], label='ECL_with_NTG_NO_FALUTS')
#plt.plot(ecl_pav3[:,0], ecl_pav3[:,1], label='ECL_with_NTG_with_FALUTS')
#err= pav/1e5-ecl_pav[0:pav.size:,1]
#plt.xcorr()
#plt.xcorr(ecl_pav[0:pav.size:, 0], err, usevlines=True, maxlags=50, normed=True, lw=2)
#plt.errorbar(ecl_pav[0:pav.size:, 0], err, yerr=err, fmt='ko')# usevlines=True, maxlags=50, normed=True, lw=2)
ymin=min(opm_pav.min()/1e5, ecl_pav[:,1].min())
ymax=max(opm_pav.max()/1e5, ecl_pav[:,1].max())
plt.ylim(264, 270)
plt.grid(True)
plt.title("FPR In OPM and ECL")
plt.legend(loc='best')
plt.xlabel("Time/Day")
plt.ylabel("FPR(bar)")
plt.show()
