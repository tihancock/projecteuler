prime_factors=[]
number=600851475143
i=2

while number!=1:
    if (number%i==0):
        prime_factors.append(i)
        number/=i
    i+=1

print prime_factors[-1]
