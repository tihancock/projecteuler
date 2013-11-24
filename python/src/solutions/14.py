longest_seq=0
n=0
i=1

while i < 1000000:
    num = i
    seq = 0
    
    while num != 1:
        if (num%2==0):
            num/=2
        else:
            num=3*num+1
        seq+=1
    
    if (seq>longest_seq):
        longest_seq=seq
        n=i

    i+=1
    
print n
        
