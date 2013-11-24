# Construct a list of fibonacci numbers not greater than 4 million
fibonacci=[1, 2]
while(fibonacci[-1] + fibonacci[-2] <= 4000000):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Print the sum of the even numbers    
print sum([i for i in fibonacci if i%2==0])
