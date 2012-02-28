Pentagons=set([n*(3*n-1)/2 for n in range(1,100000)])
Triangles=set([n*(n+1)/2 for n in range(1,100000)])
Hexagons=set([n*(2*n-1) for n in range(1,100000)])

print max(Triangles.intersection(Pentagons,Hexagons))

