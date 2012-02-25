Pentagons=[n*(3*n-1)/2 for n in range(1,100000)]
Pentagon_set=set(Pentagons)
#print [p for p in Pentagons and q for q in Pentagons if p+q in set(Pentagons) and p-q in set(Pentagons)]

for p in Pentagons:
    for q in Pentagons:
        if p+q in Pentagon_set and p-q in Pentagon_set:
            print  abs(p-q)
