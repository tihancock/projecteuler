count=0

for n in range(1,1000):
    i=1
    length=0
    while length <= n:
        length = len(str(i**n))
        if length==n:
            count+=1
        i+=1

print count
