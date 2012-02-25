n=2
count=1
sum=count

while(n<1001):
    for i in range(4):
        count+=n
        sum+=count
    n+=2
    
print sum
