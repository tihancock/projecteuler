max_sum=0

for a in range(100):
    for b in range(100):
        sum_of_digits=sum([int(i) for i in str(a**b)])
        
        if sum_of_digits > max_sum:
            max_sum = sum_of_digits

print max_sum
