"""
Calculate the line number of the largest number in the base_exp.txt file, where
each number is represented as a base exponent pair. To find this number
calculate how many digits are required for each number with exp*log(base).
"""

from math import log
from string import split

lines=split(open('files/base_exp.txt','r').read(),'\r\n')

max_num_line_num=-1
max_num_digits=0

for i in range(len(lines)):
    base_exp=[float(j) for j in split(lines[i],',')]
           
    if base_exp[1]*log(base_exp[0], 10) > max_num_digits:
        max_num_digits=base_exp[1]*log(base_exp[0], 10)
        max_num_line_num=int(i)+1

print max_num_line_num
