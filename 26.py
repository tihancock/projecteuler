import re
from fractions import Fraction
from decimal import Decimal

largest_len=0
result=0
r = re.compile(r"([0-9]{7,}?)\1+")

for n in range (2, 1000):
    s_division=""
    num=1
    re_len=0

    while num < n:
        num*=10

    while len(r.findall(s_division))==0:
        if num < n:
            next_num=0
            num*=10
        else:
            next_num=int(num/n)
            num%=n
            num*=10

        s_division+=str(next_num)

    print n

    if len(r.findall(s_division)[0]) > largest_len:
        largest_len=len(r.findall(s_division)[0])
        result=n

print result
