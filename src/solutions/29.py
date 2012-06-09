from CommonUtils import *

if __name__=="__main__":
    enumerated=[]

    for a in range(2,101):
        for b in range(2,101):
            enumerated.append(str(pow(a,b)))
        
    print len(uniqify(enumerated))
