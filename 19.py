first_day=2 #tuesday
year=1901
num_sundays=0

while year != 2001:
    if year%4==0:
        first_of_months=[0,31,60,91,121,152,182,213,244,274,305,335]
    else:
        first_of_months=[0,31,59,90,120,151,181,212,243,273,304,334]
        
    num_sundays+=len([i for i in first_of_months if i%7==first_day])

    if year%4==0:
        first_day=(first_day+366%7)%7
    else:
        first_day=(first_day+365%7)%7

    year+=1

print num_sundays


