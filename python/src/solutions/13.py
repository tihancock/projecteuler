import string

lines=string.split(open('files/100_50_digit_nums.txt', 'r').read(), "\n")

print str(sum([int(i) for i in lines]))[:10:]
