from CommonUtils import *
import sys

i=9

while 1:
    if not isPrime(i):
        canBeExpressed=False
        for j in range(1,i):
            if isPrime(i-2*j**2):
                canBeExpressed=True

        if not canBeExpressed:
            print i
            sys.exit()
    i+=2
