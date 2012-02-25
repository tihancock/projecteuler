import itertools
import sys

i=0

for l_perm in itertools.permutations(range(10),10):
    i+=1
    if i==1000000:
        print ''.join(map(str,l_perm))
        sys.exit()
