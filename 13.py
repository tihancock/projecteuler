import string

lines=string.split(open('/home/tom/Projects/ProjectEuler/files/100_50_digit_nums.txt', 'r').read(), "\n")

print sum([int(i) for i in lines])
