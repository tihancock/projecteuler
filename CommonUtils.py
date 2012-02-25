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
