import re
from fractions import Fraction
from decimal import *

getcontext().prec=2000

largest_len=0
result=0
r = re.compile(r"([0-9]{7,}?)\1+")

for n in range (2, 1000):
    unit_fraction=Decimal(1)/Decimal(n)

    matches=r.findall(str(unit_fraction))
    if len(matches) > 0:
        pattern=max(matches)

        if len(pattern) > largest_len:
            largest_len=len(pattern)
            result=n

print result
