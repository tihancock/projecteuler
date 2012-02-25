# Find the smallest number divisible by 1..20
product=1
numbers=[]

for i in range (2, 21):
    num=i
    if product%num!=0:
        for j in numbers:
            if num%j==0:
                num/=j
        
        product*=num
        numbers.append(num)
        
print product
