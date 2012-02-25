def P(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    for p in P(n-1):        
        p.append(1)
        yield p
        p.pop()
        if p and (len(p) < 2 or p[-2] > p[-1]):
            p[-1] += 1
            yield p
            
i=0

while sum(1 for _ in P(i))%1000000 != 0:
   i+=1

print i
