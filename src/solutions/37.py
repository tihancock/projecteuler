import string
from CommonUtils import isPrime

primes = [int(i) for i in string.split(open('files/primes1.txt','r').read())]

num_found=0
summation=0
i=4

while num_found<11:
    truncatable=True

    s_prime=str(primes[i])
    for n in range(1,len(s_prime)):
        if not isPrime(int(s_prime[n::])) or not isPrime(int(s_prime[:-n:])):
            truncatable=False

    if truncatable:
        summation+=primes[i]
        num_found+=1

    i+=1
                                                       
print summation
