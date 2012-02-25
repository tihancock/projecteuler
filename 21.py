summation=0

for n in range(1, 10000):
    divisor_sum=sum([i for i in range(1, n) if n%i==0])
    if (divisor_sum!=n and sum([i for i in range(1, divisor_sum) if divisor_sum%i==0])==n):
        summation+=n

print summation
