import math

factorialed=str(math.factorial(100))

print sum([int(factorialed[i]) for i in range(len(factorialed))])
