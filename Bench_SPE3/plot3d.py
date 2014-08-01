#!/usr/bin/env python

import numpy as np
from  matplotlib import cm
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Aes3d

import argparse

parser = argparse.ArgumentParser(description="Read Ecl output files")
parser.add_argument('-e', '--eclfn', help="Name of ecl file", default=None, required=True)
parser.add_argument('-o', '--opmfn', help="Name of opm file", default=None, required=True)
args = parser.parse_args()
ecl = ecl.EclFile(args.eclfn)
ecl_sw = np.array(filen["SWAT"][0])
ecl_sg = np.array(filen["SGAS"][0])

opm_sw = np.loadtxt('ecl_result/c0.txt')
tmp = np.loadtxt(args.swn)
opm_sw = np.zeros(int(len(tmp)/3))
opm_so = np.zeros(int(len(tmp)/3))
opm_sg = np.zeros(int(len(tmp)/3))
for i in xrange(len(opm_sw)):
    opm_sw[i] = tmp[3*i]
    opm_so[i] = tmp[3*i+1]
    opm_sg[i] = tmp[3*i+2]


x = np.arange(0, 100, 10)
y = np.arange(0, 100, 10)
X,Y=np.meshgrid(x,y)
Z = opm_sw-ecl_sw.reshape((10,10))
fig = plt.figure()
ax = fig.gca(projection='3d')
#N=np.arange(0, 1, 0.01)
colors = cm.jet
pic = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=colors, linewidth=0, antialiased=False,shade=False)
clevels=np.linspace(Z.min(), Z.max(), 10)
#plt.contourf(X, Y, Z, clevels, cmap=cm.jet)
plt.colorbar(pic)
plt.show()
