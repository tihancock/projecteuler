from CommonUtils import *
import sys, time, string

primes = set([int(i) for i in string.split(open('files/primes1.txt','r').read())])

n=2
pfs=[0,0,1]

while 1:
    num_pf=0
    num=n+3

    for i in range (1,int(num/2)):
        if i in primes:
            if num%i==0:
                num_pf+=1
                num/=i
    pfs.append(num_pf)
    
    if pfs[0]==4 and pfs[1]==4 and pfs[2]==4 and pfs[3]==4:
        print n
        sys.exit()

    if n%5000==0:
        print time.clock()

#    print pfs

    n+=1
    pfs.pop(0)
