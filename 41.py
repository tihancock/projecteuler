import itertools
import sys
from CommonUtils import *

for n in range(1,10)[::-1]:
    for pandigital in itertools.permutations(range(1,n)[::-1],  n-1):
        if isPrime(int(''.join(map(str,pandigital)))):
            print ''.join(map(str,pandigital))
            sys.exit()
