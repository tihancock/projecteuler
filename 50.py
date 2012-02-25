from CommonUtils import isPrime
import string

primes = [int(i) for i in string.split(open('/home/tom/Projects/ProjectEuler/files/primes1.txt','r').read())]

primes_of_interest=[p for p in primes if p<1000000]

longest_seq=0
longest_seq_prime=-1

print len(primes_of_interest)

for p in range(len(primes_of_interest)):
    summation=0
    i=p
    while i<len(primes_of_interest):
        summation+=primes_of_interest[i]

        if summation<1000000 and isPrime(summation) and i-p>longest_seq:
            longest_seq=i-p
            longest_seq_prime=summation
            print summation

        i+=1
