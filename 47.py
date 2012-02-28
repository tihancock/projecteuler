from CommonUtils import *
import sys, string

n=2
pfs=[0,0,1]

while 1:
    pfs.append(numPrimeFactors(n+3))
        
    if pfs[0]==4 and pfs[1]==4 and pfs[2]==4 and pfs[3]==4:
        print n
        sys.exit()
                
    n+=1
    pfs.pop(0)
