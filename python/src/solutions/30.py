summation=0

for n in range(2,1000000):
    digits=[int(i) for i in str(n)]
    if sum([i**5 for i in digits])==n:
        summation+=n

print summation
