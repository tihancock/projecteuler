from CommonUtils import *
import sys, time, string

primes = set([int(i) for i in string.split(open('/home/tom/Projects/ProjectEuler/files/primes1.txt','r').read())])

n=2
pfs=[0,0,1]

while 1:
    num_pf=0

    for i in range (1,int((n+3)/2)):
        if i in primes:
            if (n+3)%i==0:
                num_pf+=1
    pfs.append(num_pf)
    
    if pfs[0]==4 and pfs[1]==4 and pfs[2]==4 and pfs[3]==4:
        print n
        sys.exit()

    if n%5000==0:
        print time.clock()

#    print pfs

    n+=1
    pfs.pop(0)
