from CommonUtils import *

def sumOfFactors(num):
    return sum([i for i in range(1, num) if num%i==0])
    
abundant_nums=[]
sums_of_abundant_nums=[]
    
for i in range (1, 28123):
    if (sumOfFactors(i)>i):
        abundant_nums.append(i)
        sums_of_abundant_nums.extend([i+j for j in abundant_nums if i+j<28123])

print sum(range(28123)) - sum(uniqify(sums_of_abundant_nums))
