from math import *
from CommonUtils import *

if __name__=="__main__":
    largest=0
    product=0
    for a in range(-999,1000):
        for b in range(-999, 1000):
            n=0
            while(n**2+a*n+b>0 and isPrime(n**2+a*n+b)):
                n+=1
            if n>largest:
                largest=n
                product=a*b
    
    print product
