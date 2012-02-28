from CommonUtils import isPrime
from itertools import permutations
from fractions import Fraction
import string, sys

primes_of_interest=[i for i in range(1000,10000) if isPrime(i)]

for p in primes_of_interest:
    l_primes=[p]
    
    for perm in permutations(str(p),len(str(p))):
        int_perm = int("".join(perm))
        if int_perm in primes_of_interest and int_perm > p:
            l_primes.append(int_perm)

    sorted_primes=sorted(l_primes)
    diffs=[i-p for i in sorted_primes]

    for i in range(1,len(diffs)):
        for j in range(1,len(diffs)):
            if Fraction(diffs[j],diffs[i])==Fraction(2):
                candidate=str(p)+str(sorted_primes[i])+str(sorted_primes[j])
                # Check that the solution is not the given example
                if candidate!="148748178147":
                    print candidate
                    sys.exit()
