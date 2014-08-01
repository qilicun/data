#!/usr/bin/env python 

import argparse
import matplotlib.pyplot as plt
import ert.ecl.ecl as ecl

parser = argparse.ArgumentParser(description="Ectract OPM results")
args, unknown = parser.parse_known_args()

#sum_opm = ecl.EclSum("/project/eor/user/liuming/task/data/modified_spe9/spe9data/output_opm_spe9/BENCH_SPE9_MODIFIED")
sum_opm = ecl.EclSum("/project/eor/user/liuming/task/data/modified_spe9/spe9data/output/BENCH_SPE9_MODIFIED")
sum_ecl = ecl.EclSum("/project/eor/user/liuming/task/data/modified_spe9/spe9data/ecl/BENCH_SPE9_MODIFIED") 

vectorfield=[]
for v in unknown:
    vectorfield.append(v)

def extract_data():
    vector = ["WBHP", "WWPR", "WOPR", "WGPR"]
    opm_data={}
    ecl_data={}
    ecl_data["time"]=sum_ecl.days
    opm_data["time"]=sum_opm.days
    for v in vector:
        opm_data[str(v)]=sum_opm.get_values(v+":"+unknown[0])
        ecl_data[str(v)]=sum_ecl.get_values(v+":"+unknown[0])
    for key in opm_data:
        if key=="WBHP":
            print "found WBHP"
            tmp=opm_data[key]
            tmp = tmp * 0.000145037738
            del opm_data[key]
            opm_data[key] = tmp
        if key=="WGPR":
            print "found WGPR"
            tmp=opm_data[key]
            tmp=tmp * 3051187.4976505954
            del opm_data[key]
            opm_data[key] = tmp

    opm_data["WWCT"]=opm_data["WWPR"]/(opm_data["WWPR"]+opm_data["WOPR"])
    opm_data["WGOR"]=opm_data["WGPR"]/opm_data["WOPR"]
    ecl_data["WWCT"]=sum_ecl.get_values("WWCT:"+unknown[0])
    ecl_data["WGOR"]=sum_ecl.get_values("WGOR:"+unknown[0])
    
    return opm_data, ecl_data

def plot(vec):
    for v in vec:
        plt.figure()
        plt.plot(ecl_data["time"], ecl_data[v], 'r')
        plt.plot(opm_data["time"], opm_data[v], 'b')
        plt.grid(b=True, which='both', color='0.65',linestyle='-')
        plt.xlabel("Days")
        plt.title(v+":"+unknown[0])
        plt.legend(["ECL", "OPM"], loc="best")
    plt.show()
opm_data, ecl_data=extract_data()
print opm_data["WGPR"]
plotvec=["WBHP", "WWCT", "WGOR", "WGPR", "WWPR", "WOPR"]
plot(plotvec)
