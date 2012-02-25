from numpy import *

upper_limit=2000000
sqrt_upper_limit=int(sqrt(upper_limit))+1

flags=zeros(upper_limit)+1

for n in range(2, sqrt_upper_limit):
    flags[n*n::n]=0

sum=0
for n in range(2, len(flags)):
    sum+=n*flags[n]
        
print int(sum)

# Gets some kind of integer overflow problem
# print sum(flatnonzero(flags)[2:])
