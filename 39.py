solutions=[0]*1000

for a in range(1,1000):
    for b in range(1,1000-a):
        for c in range(1,1000-(a+b)):
            if a**2+b**2==c**2 and a+b+c<=1000:
                solutions[a+b+c-1]+=1

print solutions.index(max(solutions))+1
