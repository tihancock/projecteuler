import sys

x=1

while 1:
    times1=set(map(int,str(x)))
    
    if times1==set(map(int,str(2*x))) and \
    times1==set(map(int,str(3*x))) and \
    times1==set(map(int,str(4*x))) and \
    times1==set(map(int,str(5*x))) and \
    times1==set(map(int,str(6*x))):
        print x
        sys.exit()

    x+=1
