from CommonUtils import *
    
def isPandigital1Through9(sorted_seq):
    if (sorted_seq==['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        return True
    else:
        return False

if __name__=="__main__":
    pandigitals=[]
    
    for a in range(2000):
        for b in range(1000):
            if isPandigital1Through9(sorted(list(str(a))+list(str(b))+list(str(a*b)))):
                pandigitals.append(a*b)
                
    print(sum(uniqify(pandigitals)))
