import string
from CommonUtils import *

if __name__=="__main__":
    largest_pandig=0
    i=0
    
    while i<10000:
        for n in range(3, 10):
            candidate=string.join([str(i*j) for j in range (1, n)],"")
            if int(candidate)>largest_pandig and int(candidate) <= 987654321:
                if isPandigital1Through9(sorted(candidate)):
                    largest_pandig=int(candidate)
                    
        i+=1
        
    print largest_pandig
    
