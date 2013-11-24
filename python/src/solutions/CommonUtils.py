""" Utility functions used often enough to merit inclusion here """
from math import sqrt

def uniqify(seq):
    """ Returns the supplied list with duplicates removed """
    # not order preserving 
    set = {} 
    map(set.__setitem__, seq, []) 
    return set.keys()

def isPrime (n):
    """ Returns True if the supplied integer is prime, false otherwise """
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def numPrimeFactors(n):
    """ Returns the number of prime factors of n """
    num_pfs=0
    i=2
    while n!=1:
        if n%i==0:
            num_pfs+=1
            while n%i==0:
                n/=i
            
        i+=1

    return num_pfs

def isPandigital1Through9(sorted_seq):
    if (sorted_seq==['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        return True
    else:
        return False
