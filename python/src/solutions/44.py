import sys

Pentagons=set([n*(3*n-1)/2 for n in range(1,5000)])

for p in Pentagons:
    for q in Pentagons:
        if p+q in Pentagons and p-q in Pentagons:
            print abs(p-q)
            sys.exit()
