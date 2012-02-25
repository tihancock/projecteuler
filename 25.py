F_n_2=1
F_n_1=1
n=2

while len(str(F_n_1))<1000:
    temp=F_n_1+F_n_2
    F_n_2=F_n_1
    F_n_1=temp
    n+=1
    
print n
