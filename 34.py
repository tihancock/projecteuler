from math import *

summation=0

for i in range(100000):
    digits=list(str(i))
    if (len(digits)>1 and sum([factorial(int(x)) for x in digits])==i):
        print i
        summation+=i
        
print summation
