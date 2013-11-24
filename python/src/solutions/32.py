from CommonUtils import *
    
if __name__=="__main__":
    pandigitals=[]
    
    for a in range(2000):
        for b in range(1000):
            if isPandigital1Through9(sorted(list(str(a))+list(str(b))+list(str(a*b)))):
                pandigitals.append(a*b)
                
    print(sum(uniqify(pandigitals)))
