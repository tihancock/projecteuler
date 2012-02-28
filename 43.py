from itertools import permutations

primes=[2,3,5,7,11,13,17]
summation=0

for i in permutations('1234567890', 10):
    has_property=True

    for j in range(1,8):
        if int(i[j]+i[j+1]+i[j+2])%primes[j-1]!=0:
            has_property=False
            
    if has_property:
        summation+=int("".join(i))

print summation
