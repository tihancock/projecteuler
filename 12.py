from math import *

i=0
triangle_n=0
divisor_len=0
while (divisor_len < 500):
    divisor_len=0
    j=1
    i+=1
    triangle_n+=i
    while j < int(sqrt(triangle_n+1)):
        if triangle_n%j==0:
            divisor_len+=2
        j+=1
    
print triangle_n
