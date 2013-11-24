# Find the 10001st prime number
from CommonUtils import isPrime

n,num_primes=0,0

while(num_primes < 10001):
    n+=1
    if isPrime(n):
        num_primes+=1

print n
