from CommonUtils import isPrime
import string

primes = [int(i) for i in string.split(open('files/primes1.txt','r').read())]

primes_of_interest=[p for p in primes if p<1000000]
set_of_primes=set(primes_of_interest) # For swift primality checks

longest_seq=0
longest_seq_prime=-1

for p in range(1000000):
    summation=0
    i=p
    while i < len(primes_of_interest) and summation < 1000000:
        summation+=primes_of_interest[i]

        if summation in set_of_primes and i-p > longest_seq:
            longest_seq=i-p
            longest_seq_prime=summation

        i+=1

print longest_seq_prime
