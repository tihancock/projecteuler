from fractions import Fraction

result=Fraction(1,1)

for j in range(10,100):
    for i in range(10,j):
        i_1=int(str(i)[0])
        i_2=int(str(i)[1])
        j_1=int(str(j)[0])
        j_2=int(str(j)[1])

        if i_2==0 or j_2==0:
            continue
        
        if i_1==j_1 and Fraction(i_2,j_2)==Fraction(i,j) or \
            i_1==j_2 and Fraction(i_2,j_1)==Fraction(i,j) or \
            i_2==j_1 and Fraction(i_1,j_2)==Fraction(i,j) or \
            i_2==j_2 and Fraction(i_1,j_1)==Fraction(i,j):
            result*=Fraction(i,j)

print result
            
