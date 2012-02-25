from CommonUtils import isPrime

count=0

for n in range(1000000):
    if isPrime(n):
        s_prime=str(n)
        all_prime=True

        for i in range(len(s_prime)):
            if not isPrime(int(s_prime[-i::]+s_prime[:-i:])):
                all_prime=False

        if all_prime:
            count+=1

print count
    
