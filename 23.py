from CommonUtils import *

UPPER_LIMIT=28123

def sumOfFactors(num):
    return sum([i for i in range(1, num) if num%i==0])
    
abundant_nums=[]
sums_of_abundant_nums=[]
    
for i in range (1, UPPER_LIMIT):
    if (sumOfFactors(i)>i):
        abundant_nums.append(i)
        sums_of_abundant_nums.extend([i+j for j in abundant_nums if i+j<UPPER_LIMIT])

print sum(range(UPPER_LIMIT)) - sum(uniqify(sums_of_abundant_nums))
